# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class LeaseContract(models.Model):
    _name = 'lease.contract'
    _description = 'Tenant Lease Contract Lifecycle'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Lease Ref Number', required=True, copy=False, readonly=True, default='New')
    tenant_id = fields.Many2one('res.partner', string='Tenant Name', required=True, tracking=True)
    unit_id = fields.Many2one('property.unit', string='Assigned Unit', required=True, tracking=True)
    
    date_start = fields.Date(string='Contract Start Date', required=True)
    date_end = fields.Date(string='Contract End Date', required=True)
    
    monthly_rent = fields.Monetary(string='Monthly Rent Amount', currency_field='currency_id', required=True, tracking=True)
    security_deposit = fields.Monetary(string='Security Deposit Required', currency_field='currency_id', required=True)
    deposit_refund_amount = fields.Monetary(string='Deposit Refund Eligible', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    stage = fields.Selection([
        ('inquiry', 'Inquiry & Ocular Visit'),
        ('quotation', 'Quotation & Reservation'),
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
    
    notes = fields.Text(string='Contract Special Terms & Conditions')

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
            rec.unit_id.status = 'occupied'
            rec.unit_id.current_tenant_id = rec.tenant_id

    def action_trigger_move_out(self):
        for rec in self:
            rec.stage = 'move_out'
            rec.unit_id.status = 'maintenance'
