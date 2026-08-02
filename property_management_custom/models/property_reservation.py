# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class PropertyReservation(models.Model):
    _name = 'property.reservation'
    _description = 'Property Unit Reservation Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reservation Ref', required=True, copy=False, readonly=True, default='New')
    tenant_id = fields.Many2one('res.partner', string='Tenant / Client', required=True, tracking=True)
    unit_id = fields.Many2one(
        'product.product', 
        string='Reserved Property Unit', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )

    reservation_amount_preset = fields.Selection([
        ('5000', 'PHP 5,000 Standard Reservation Fee'),
        ('10000', 'PHP 10,000 Prime Unit Reservation Fee'),
        ('custom', 'Custom Amount'),
    ], string='Fee Structure', default='5000', tracking=True)

    reservation_amount = fields.Monetary(
        string='Reservation Amount', 
        currency_field='currency_id', 
        default=5000.0, 
        tracking=True
    )
    reservation_date = fields.Date(string='Reservation Date Paid', default=fields.Date.context_today, tracking=True)
    expiration_date = fields.Date(string='Reservation Expiry Date', tracking=True)

    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('for_verification', 'For Verification'),
        ('paid', 'Paid'),
    ], string='Payment Status', default='unpaid', tracking=True)

    proof_of_payment = fields.Binary(string='Proof of Payment Attachment')
    proof_of_payment_filename = fields.Char(string='Proof File Name')

    acknowledgement_receipt_no = fields.Char(string='Acknowledgement Receipt No.', readonly=True, copy=False, tracking=True)
    billing_copy_attached = fields.Boolean(string='Billing Copy Attached', default=False, tracking=True)
    tenant_copy_issued = fields.Boolean(string='Tenant Copy Issued', default=False, tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('for_payment', 'For Payment'),
        ('paid', 'Paid & Reserved'),
        ('expired', 'Expired'),
        ('converted', 'Converted to Lease'),
        ('cancelled', 'Cancelled'),
    ], string='Reservation Status', default='draft', tracking=True)

    opportunity_id = fields.Many2one('crm.lead', string='Associated CRM Inquiry')
    sale_order_id = fields.Many2one('sale.order', string='Quotation Ref')
    lease_contract_id = fields.Many2one('lease.contract', string='Lease Contract Ref')

    cancellation_reason = fields.Text(string='Cancellation Reason / Management Policy Notes')
    manager_approval = fields.Boolean(string='Manager Approval for Cancellation', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.ref('base.PHP', raise_if_not_found=False) or self.env.company.currency_id
    )

    @api.onchange('reservation_amount_preset')
    def _onchange_reservation_amount_preset(self):
        if self.reservation_amount_preset == '5000':
            self.reservation_amount = 5000.0
        elif self.reservation_amount_preset == '10000':
            self.reservation_amount = 10000.0

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('property.reservation') or 'RES-2026-00001'
        return super(PropertyReservation, self).create(vals)

    def action_submit_payment(self):
        for rec in self:
            if not rec.proof_of_payment:
                raise UserError("Please attach the Proof of Payment before submitting for verification.")
            rec.payment_status = 'for_verification'
            rec.state = 'for_payment'
            rec.billing_copy_attached = True
            rec.message_post(
                body=f"Reservation payment proof for <b>{rec.currency_id.symbol}{rec.reservation_amount:,.2f}</b> submitted to Billing for verification.",
                subject="Reservation Payment Submitted"
            )

    def action_confirm_payment(self):
        for rec in self:
            rec.payment_status = 'paid'
            rec.state = 'paid'
            if not rec.acknowledgement_receipt_no:
                rec.acknowledgement_receipt_no = self.env['ir.sequence'].next_by_code('property.reservation.ar') or f"AR-{rec.id:05d}"
            rec.tenant_copy_issued = True

            # Control: Unit status changes to Reserved ONLY after payment confirmation
            if rec.unit_id:
                rec.unit_id.occupancy_status = 'reserved'
                rec.unit_id.current_tenant_id = rec.tenant_id

            if rec.opportunity_id:
                rec.opportunity_id.reservation_verified = True
                rec.opportunity_id.unit_hold_status = 'hold_active'
                rec.opportunity_id.official_receipt_no = rec.acknowledgement_receipt_no

            rec.message_post(
                body=f"Payment of <b>{rec.currency_id.symbol}{rec.reservation_amount:,.2f}</b> confirmed by Finance/Billing. Acknowledgement Receipt Issued: <b>{rec.acknowledgement_receipt_no}</b>. Property Unit <b>{rec.unit_id.display_name}</b> is now locked / reserved.",
                subject="Payment Confirmed & Unit Reserved"
            )

    def action_convert_to_lease(self):
        for rec in self:
            if rec.state != 'paid':
                raise UserError("Only paid & verified reservations can be converted into an active lease contract!")
            rec.state = 'converted'
            
            # Auto-create or link Lease Contract
            if not rec.lease_contract_id:
                contract_vals = {
                    'tenant_id': rec.tenant_id.id,
                    'unit_id': rec.unit_id.id,
                    'date_start': fields.Date.context_today(self),
                    'date_end': fields.Date.add(fields.Date.context_today(self), months=12),
                    'monthly_rent': rec.unit_id.list_price or 25000.0,
                    'security_deposit': (rec.unit_id.list_price or 25000.0) * 2,
                    'stage': 'reservation',
                }
                lease = self.env['lease.contract'].create(contract_vals)
                rec.lease_contract_id = lease.id

            rec.message_post(
                body=f"Reservation converted into Lease Contract <b>{rec.lease_contract_id.name}</b>. Reservation fee of <b>{rec.currency_id.symbol}{rec.reservation_amount:,.2f}</b> applied towards lease customer advance.",
                subject="Converted to Lease Contract"
            )

    def action_approve_cancellation(self):
        for rec in self:
            rec.manager_approval = True
            rec.message_post(
                body="Manager Approval granted for Reservation Cancellation.",
                subject="Manager Approval Granted"
            )

    def action_cancel(self):
        for rec in self:
            # Control: Reservation cancellation MUST require manager approval
            if not rec.manager_approval:
                raise UserError("Reservation Cancellation Blocked: Management Approval is required before cancelling or forfeiting a reservation!")
            
            rec.state = 'cancelled'
            if rec.unit_id and rec.unit_id.occupancy_status == 'reserved':
                rec.unit_id.occupancy_status = 'available'

            rec.message_post(
                body=f"Reservation <b>{rec.name}</b> has been cancelled. Unit <b>{rec.unit_id.display_name}</b> released back to available inventory. Cancellation Reason: {rec.cancellation_reason or 'None provided'}",
                subject="Reservation Cancelled"
            )
