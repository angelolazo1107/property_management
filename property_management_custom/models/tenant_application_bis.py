# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class TenantApplicationBis(models.Model):
    _name = 'tenant.application.bis'
    _description = 'Tenant Application & Billing Information Sheet (BIS)'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='BIS Ref Number', required=True, copy=False, readonly=True, default='New')
    tenant_id = fields.Many2one('res.partner', string='Tenant Name', required=True, tracking=True)
    unit_id = fields.Many2one(
        'product.product', 
        string='Unit Number', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    contact_info = fields.Char(string='Contact Information', compute='_compute_contact_info', store=True, readonly=False)

    bare_unit_price = fields.Monetary(string='Bare Unit Price', currency_field='currency_id', tracking=True)
    furniture_rental_price = fields.Monetary(string='Furniture Rental Price', currency_field='currency_id', tracking=True)
    rental_price = fields.Monetary(string='Total Monthly Rent', currency_field='currency_id', compute='_compute_rental_price', store=True)
    security_deposit = fields.Monetary(string='Security Deposit', currency_field='currency_id', tracking=True)
    
    move_in_date = fields.Date(string='Target Move-In Date', tracking=True)
    lease_term = fields.Selection([
        ('6_months', '6 Months'),
        ('1_year', '1 Year'),
        ('2_years', '2 Years'),
        ('custom', 'Custom Term'),
    ], string='Lease Term', default='1_year', tracking=True)

    with_agent = fields.Boolean(string='With Agent', default=False, tracking=True)
    agent_id = fields.Many2one('res.partner', string='Agent Name', domain="[('is_company', '=', False)]", tracking=True)
    
    discounted_price = fields.Boolean(string='Discounted Price', default=False, tracking=True)
    discount_remarks = fields.Text(string='Discount Remarks', tracking=True)

    valid_id = fields.Binary(string='Valid ID Attachment')
    valid_id_filename = fields.Char(string='Valid ID File Name')
    proof_of_income = fields.Binary(string='Proof of Income Attachment')
    proof_of_income_filename = fields.Char(string='Proof of Income File Name')

    submitted_to_billing = fields.Boolean(string='Submitted to Billing', default=False, tracking=True)
    submitted_to_legal = fields.Boolean(string='Submitted to Legal', default=False, tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('billing_review', 'For Billing Review'),
        ('legal_review', 'For Legal Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='BIS Status', default='draft', tracking=True)

    opportunity_id = fields.Many2one('crm.lead', string='Associated CRM Lead')
    reservation_id = fields.Many2one('property.reservation', string='Associated Reservation')
    lease_contract_id = fields.Many2one('lease.contract', string='Lease Contract Reference')

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.PHP', raise_if_not_found=False) or self.env.company.currency_id
    )

    @api.depends('tenant_id')
    def _compute_contact_info(self):
        for rec in self:
            if rec.tenant_id:
                parts = [p for p in [rec.tenant_id.phone, rec.tenant_id.mobile, rec.tenant_id.email] if p]
                rec.contact_info = " | ".join(parts)
            else:
                rec.contact_info = False

    @api.depends('bare_unit_price', 'furniture_rental_price')
    def _compute_rental_price(self):
        for rec in self:
            rec.rental_price = (rec.bare_unit_price or 0.0) + (rec.furniture_rental_price or 0.0)

    @api.onchange('unit_id')
    def _onchange_unit_id(self):
        if self.unit_id:
            self.bare_unit_price = self.unit_id.list_price
            self.security_deposit = self.unit_id.list_price * 2.0

    @api.constrains('discounted_price', 'discount_remarks')
    def _check_discount_remarks(self):
        for rec in self:
            if rec.discounted_price and not rec.discount_remarks:
                raise UserError("Discount Remarks are required whenever Discounted Price is enabled!")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('tenant.application.bis') or 'BIS-2026-00001'
        return super(TenantApplicationBis, self).create(vals)

    def action_submit_billing(self):
        for rec in self:
            rec.submitted_to_billing = True
            rec.state = 'billing_review'
            rec.message_post(
                body=f"Buyer/Tenant Information Sheet (BIS) <b>{rec.name}</b> submitted to Billing team for financial review.",
                subject="Submitted to Billing"
            )

    def action_submit_legal(self):
        for rec in self:
            if not rec.valid_id or not rec.proof_of_income:
                raise UserError("Submission Blocked: Both Valid ID and Proof of Income attachments are required before submitting to Legal!")
            rec.submitted_to_legal = True
            rec.state = 'legal_review'
            rec.message_post(
                body=f"BIS Application <b>{rec.name}</b> along with Tenant ID and Proof of Income submitted to Legal for Contract Preparation.",
                subject="Submitted to Legal"
            )

    def action_approve_bis(self):
        for rec in self:
            rec.state = 'approved'
            
            # Create or Link Lease Contract
            if not rec.lease_contract_id:
                lease_vals = {
                    'tenant_id': rec.tenant_id.id,
                    'unit_id': rec.unit_id.id,
                    'date_start': rec.move_in_date or fields.Date.context_today(self),
                    'date_end': fields.Date.add(rec.move_in_date or fields.Date.context_today(self), years=1),
                    'monthly_rent': rec.rental_price,
                    'security_deposit': rec.security_deposit,
                    'stage': 'legal_review',
                    'bis_submitted': True,
                }
                lease = self.env['lease.contract'].create(lease_vals)
                rec.lease_contract_id = lease.id

            # Initialize Tenant Document Subfolders
            if hasattr(self.env['property.document.category'], 'create_tenant_subfolders'):
                self.env['property.document.category'].create_tenant_subfolders(
                    property_name=rec.unit_id.name or 'Property',
                    unit_name=rec.unit_id.name or 'Unit',
                    tenant_name=rec.tenant_id.name
                )

            if rec.opportunity_id:
                rec.opportunity_id.bis_status = 'verified'

            rec.message_post(
                body=f"BIS Application <b>{rec.name}</b> Approved. Lease Contract <b>{rec.lease_contract_id.name}</b> prepared and document folders initialized.",
                subject="BIS Approved & Contract Prepared"
            )

    def action_reject_bis(self):
        for rec in self:
            rec.state = 'rejected'
            if rec.opportunity_id:
                rec.opportunity_id.bis_status = 'rejected'
            rec.message_post(
                body=f"BIS Application <b>{rec.name}</b> has been rejected.",
                subject="BIS Application Rejected"
            )
