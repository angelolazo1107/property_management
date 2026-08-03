# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class MoveOutClearance(models.Model):
    _name = 'move.out.clearance'
    _description = 'Move-Out Clearance & Departmental Sign-Off'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Clearance Ref', 
        required=True, 
        copy=False, 
        readonly=True, 
        default='New'
    )
    tenant_id = fields.Many2one(
        'res.partner', 
        string='Tenant Name', 
        required=True, 
        tracking=True
    )
    unit_id = fields.Many2one(
        'product.product', 
        string='Unit Number', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    lease_contract_id = fields.Many2one(
        'lease.contract', 
        string='Lease Contract Reference', 
        required=True, 
        tracking=True
    )

    move_out_date = fields.Date(
        string='Move-Out Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )
    reason = fields.Selection([
        ('end_of_lease', 'End of Lease Contract'),
        ('early_termination', 'Early Pre-Termination'),
        ('breach', 'Contract Breach / Unnotified Exit'),
    ], string='Reason for Move-Out', default='end_of_lease', required=True, tracking=True)

    notice_date = fields.Date(string='Notice Date (Tenant Notified)', tracking=True)
    notice_compliance = fields.Selection([
        ('compliant', 'Compliant (7+ Days Notice)'),
        ('non_compliant', 'Not Compliant (Short Notice)'),
    ], string='Notice Compliance', compute='_compute_notice_compliance', store=True, tracking=True)

    outstanding_balance = fields.Monetary(
        string='Outstanding Balance (Rent/Charges)', 
        currency_field='currency_id', 
        tracking=True
    )
    final_inspection_status = fields.Selection([
        ('pending', 'Pending Inspection'),
        ('passed', 'Passed (Clean / No Damage)'),
        ('with_damage', 'With Damage / Missing Items'),
    ], string='Final Inspection Status', default='pending', tracking=True)

    damage_charges = fields.Monetary(string='Damage & Repair Charges', currency_field='currency_id', tracking=True)
    utility_charges = fields.Monetary(string='Utility Unbilled Charges', currency_field='currency_id', tracking=True)
    other_deductions = fields.Monetary(string='Other Deductions', currency_field='currency_id', tracking=True)

    security_deposit = fields.Monetary(string='Security Deposit Amount', currency_field='currency_id', tracking=True)
    refundable_amount = fields.Monetary(
        string='Net Refundable Amount (PHP)', 
        currency_field='currency_id', 
        compute='_compute_refundable_amount', 
        store=True, 
        tracking=True
    )

    deposit_forfeited = fields.Boolean(string='Deposit Forfeited?', default=False, tracking=True)
    forfeiture_reason = fields.Text(string='Forfeiture Justification / Reason')

    # 8-Departmental Move-Out Checklist Items
    clearance_billing = fields.Boolean(string='1. Billing Clearance: No outstanding rent or charges', tracking=True)
    clearance_admin = fields.Boolean(string='2. Admin Clearance: Unit turnover inspected', tracking=True)
    clearance_housekeeping = fields.Boolean(string='3. Housekeeping Clearance: Cleanliness verified', tracking=True)
    clearance_it = fields.Boolean(string='4. IT Clearance: Wi-Fi router & modem returned', tracking=True)
    clearance_security = fields.Boolean(string='5. Security Clearance: Access card returned & gate pass issued', tracking=True)
    clearance_parking = fields.Boolean(string='6. Parking Clearance: Sticker & parking slot cleared', tracking=True)
    clearance_legal = fields.Boolean(string='7. Legal Clearance: Breach & pre-termination terms reviewed', tracking=True)
    clearance_finance = fields.Boolean(string='8. Finance Clearance: Deposit refund or forfeiture processed', tracking=True)

    clearance_status = fields.Selection([
        ('draft', 'Draft Clearance'),
        ('for_inspection', 'For Inspection'),
        ('for_billing_clearance', 'For Departmental Clearances'),
        ('cleared', 'Cleared for Exit'),
        ('closed', 'Closed & Terminated'),
    ], string='Clearance Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Move-Out Remarks & Special Provisions')

    @api.depends('notice_date', 'move_out_date')
    def _compute_notice_compliance(self):
        for rec in self:
            if rec.notice_date and rec.move_out_date:
                days_notice = (rec.move_out_date - rec.notice_date).days
                rec.notice_compliance = 'compliant' if days_notice >= 7 else 'non_compliant'
            else:
                rec.notice_compliance = 'non_compliant'

    @api.depends('security_deposit', 'outstanding_balance', 'damage_charges', 'utility_charges', 'other_deductions', 'deposit_forfeited')
    def _compute_refundable_amount(self):
        for rec in self:
            if rec.deposit_forfeited:
                rec.refundable_amount = 0.0
            else:
                total_deductions = (
                    (rec.outstanding_balance or 0.0) +
                    (rec.damage_charges or 0.0) +
                    (rec.utility_charges or 0.0) +
                    (rec.other_deductions or 0.0)
                )
                net = (rec.security_deposit or 0.0) - total_deductions
                rec.refundable_amount = max(0.0, net)

    @api.onchange('lease_contract_id')
    def _onchange_lease_contract_id(self):
        if self.lease_contract_id:
            self.tenant_id = self.lease_contract_id.tenant_id
            self.unit_id = self.lease_contract_id.unit_id
            self.security_deposit = self.lease_contract_id.security_deposit
            if hasattr(self.tenant_id, 'tenant_unpaid_balance'):
                self.outstanding_balance = self.tenant_id.tenant_unpaid_balance

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('move.out.clearance') or 'MCLR-2026-00001'
        return super(MoveOutClearance, self).create(vals)

    def action_submit_inspection(self):
        for rec in self:
            rec.clearance_status = 'for_inspection'
            rec.message_post(
                body=f"Move-Out Clearance <b>{rec.name}</b> submitted for turnover inspection on Unit {rec.unit_id.name}.",
                subject="Inspection Scheduled"
            )

    def action_complete_inspection(self):
        for rec in self:
            rec.clearance_status = 'for_billing_clearance'
            rec.message_post(
                body=f"Unit turnover inspection completed. Final Status: <b>{rec.final_inspection_status.title()}</b>. Forwarded for 8-Departmental sign-offs.",
                subject="Inspection Completed"
            )

    def action_grant_clearance(self):
        for rec in self:
            missing_checklists = []
            if not rec.clearance_billing: missing_checklists.append("1. Billing")
            if not rec.clearance_admin: missing_checklists.append("2. Admin")
            if not rec.clearance_housekeeping: missing_checklists.append("3. Housekeeping")
            if not rec.clearance_it: missing_checklists.append("4. IT")
            if not rec.clearance_security: missing_checklists.append("5. Security")
            if not rec.clearance_parking: missing_checklists.append("6. Parking")
            if not rec.clearance_legal: missing_checklists.append("7. Legal")
            if not rec.clearance_finance: missing_checklists.append("8. Finance")

            if missing_checklists:
                raise UserError(f"Departmental Sign-Off Incomplete: The following 8-departmental clearances are required before granting move-out exit clearance: {', '.join(missing_checklists)}!")

            if rec.deposit_forfeited and not rec.forfeiture_reason:
                raise UserError("Forfeiture Justification Required: Please enter the official reason for security deposit forfeiture!")

            rec.clearance_status = 'cleared'
            rec.message_post(
                body=f"🎉 <b>FINAL MOVE-OUT EXIT CLEARANCE GRANTED</b> for Tenant <b>{rec.tenant_id.name}</b> [Unit: {rec.unit_id.name}]. Net Refundable Deposit: PHP {(rec.refundable_amount or 0.0):,.2f}.",
                subject="Move-Out Clearance Granted"
            )

    def action_close(self):
        for rec in self:
            rec.clearance_status = 'closed'
            if rec.lease_contract_id:
                rec.lease_contract_id.stage = 'terminated'
            rec.message_post(
                body=f"Move-Out File <b>{rec.name}</b> CLOSED. Lease Contract <b>{rec.lease_contract_id.name}</b> marked as Terminated.",
                subject="Move-Out File Closed"
            )
