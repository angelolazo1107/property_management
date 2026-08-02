# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class LeaseContract(models.Model):
    _name = 'lease.contract'
    _description = 'Tenant Lease Contract Lifecycle'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Lease Ref Number', required=True, copy=False, readonly=True, default='New')
    tenant_id = fields.Many2one('res.partner', string='Tenant Name', required=True, tracking=True)
    unit_id = fields.Many2one('product.product', string='Assigned Property Unit', domain="[('is_property_unit', '=', True)]", required=True, tracking=True)
    
    date_start = fields.Date(string='Contract Start Date', required=True)
    date_end = fields.Date(string='Contract End Date', required=True)
    
    monthly_rent = fields.Monetary(string='Monthly Rent Amount', currency_field='currency_id', required=True, tracking=True)
    security_deposit = fields.Monetary(string='Security Deposit Required', currency_field='currency_id', required=True)
    
    stage = fields.Selection([
        ('inquiry', 'Inquiry & Ocular Visit'),
        ('reservation', 'Quotation & Reservation'),
        ('bis_submitted', 'BIS Submitted'),
        ('legal_review', 'Legal Contract Review'),
        ('payment_clearance', 'Accounting Payment Clearance'),
        ('active', 'Active Lease'),
        ('renewal_notice', 'Renewal Notice Sent'),
        ('move_out', 'Move-Out Inspection'),
        ('final_billing', 'Final Billing Settlement'),
        ('deposit_refund', 'Security Deposit Refunded'),
        ('terminated', 'Closed / Terminated'),
    ], string='Lease Lifecycle Stage', default='inquiry', tracking=True)

    bis_submitted = fields.Boolean(string='BIS Data Verified')
    legal_clearance = fields.Boolean(string='Legal Clearance Approved')
    deposit_paid = fields.Boolean(string='Security Deposit Paid (Accounting Verified)', tracking=True)
    move_in_checklist_done = fields.Boolean(string='PMO Move-In Checklist Completed')
    
    # Move-Out & Deposit Settlement Ledger
    unpaid_rent_deduction = fields.Monetary(string='Unpaid Rent Deduction', currency_field='currency_id')
    utility_deduction = fields.Monetary(string='Utility Deduction', currency_field='currency_id')
    damage_deduction = fields.Monetary(string='Damage Charges Deduction', currency_field='currency_id')
    cleaning_deduction = fields.Monetary(string='Cleaning Charges Deduction', currency_field='currency_id')
    penalties_deduction = fields.Monetary(string='Penalties / Late Charges', currency_field='currency_id')
    missing_items_deduction = fields.Monetary(string='Missing Access Items Deduction', currency_field='currency_id')
    
    total_deductions = fields.Monetary(string='Total Deductions', currency_field='currency_id', compute='_compute_deductions', store=True)
    net_refund_amount = fields.Monetary(string='Net Security Deposit Refundable', currency_field='currency_id', compute='_compute_net_refund', store=True)
    
    deposit_refund_status = fields.Selection([
        ('pending', 'Pending Clearance'),
        ('approved', 'Refund Approved by GM'),
        ('processed', 'Accounting Voucher Prepared'),
        ('refunded', 'Deposit Refund Released'),
    ], string='Security Deposit Refund Status', default='pending', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.PHP', raise_if_not_found=False) or self.env.company.currency_id
    )
    notes = fields.Text(string='Contract Special Terms & Conditions')

    @api.depends('unpaid_rent_deduction', 'utility_deduction', 'damage_deduction', 'cleaning_deduction', 'penalties_deduction', 'missing_items_deduction')
    def _compute_deductions(self):
        for rec in self:
            rec.total_deductions = (
                rec.unpaid_rent_deduction +
                rec.utility_deduction +
                rec.damage_deduction +
                rec.cleaning_deduction +
                rec.penalties_deduction +
                rec.missing_items_deduction
            )

    @api.depends('security_deposit', 'total_deductions')
    def _compute_net_refund(self):
        for rec in self:
            rec.net_refund_amount = max(0.0, rec.security_deposit - rec.total_deductions)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('lease.contract') or 'LEASE-00001'
        return super(LeaseContract, self).create(vals)

    def action_verify_payment_clearance(self):
        for rec in self:
            if not rec.deposit_paid:
                raise UserError("Payment Clearance Blocked: Accounting must verify the security deposit receipt before move-in approval!")
            rec.stage = 'active'
            rec.unit_id.occupancy_status = 'occupied'
            rec.unit_id.current_tenant_id = rec.tenant_id

    def action_trigger_move_out(self):
        for rec in self:
            rec.stage = 'move_out'
            rec.unit_id.occupancy_status = 'vacated'

    def action_approve_deposit_refund(self):
        for rec in self:
            rec.deposit_refund_status = 'approved'
            rec.stage = 'deposit_refund'
