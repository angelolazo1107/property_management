# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class SecurityDepositRefund(models.Model):
    _name = 'security.deposit.refund'
    _description = 'Security Deposit Refund & Accounting Settlement'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Refund Ref', 
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
    move_out_clearance_id = fields.Many2one(
        'move.out.clearance', 
        string='Move-Out Clearance Reference', 
        tracking=True
    )

    original_security_deposit = fields.Monetary(
        string='Original Security Deposit', 
        currency_field='currency_id', 
        required=True, 
        tracking=True
    )
    outstanding_rent_deduction = fields.Monetary(
        string='Outstanding Rent Deduction', 
        currency_field='currency_id', 
        tracking=True
    )
    damage_deduction = fields.Monetary(
        string='Damage & Repair Deduction', 
        currency_field='currency_id', 
        tracking=True
    )
    utility_deduction = fields.Monetary(
        string='Utility Unbilled Deduction', 
        currency_field='currency_id', 
        tracking=True
    )
    other_deduction = fields.Monetary(
        string='Other Deductions', 
        currency_field='currency_id', 
        tracking=True
    )

    total_deduction = fields.Monetary(
        string='Total Deductions', 
        currency_field='currency_id', 
        compute='_compute_deductions_and_refund', 
        store=True, 
        tracking=True
    )
    refundable_amount = fields.Monetary(
        string='Net Refundable Amount (PHP)', 
        currency_field='currency_id', 
        compute='_compute_deductions_and_refund', 
        store=True, 
        tracking=True
    )

    bank_name = fields.Char(string='Bank Name', tracking=True)
    account_name = fields.Char(string='Bank Account Name', tracking=True)
    account_number = fields.Char(string='Bank Account Number', tracking=True)

    refund_application_date = fields.Date(
        string='Refund Application Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )
    expected_release_date = fields.Date(
        string='Expected Release Date (5-7 Working Days)', 
        compute='_compute_expected_release_date', 
        store=True, 
        tracking=True
    )

    finance_approval = fields.Selection([
        ('pending', 'Pending Finance Approval'),
        ('approved', 'Approved by Finance'),
        ('rejected', 'Rejected'),
    ], string='Finance Approval', default='pending', tracking=True)

    payment_status = fields.Selection([
        ('pending', 'Pending Payment'),
        ('in_payment', 'In Payment / Wire Processing'),
        ('paid', 'Refund Paid / Completed'),
    ], string='Payment Status', default='pending', tracking=True)

    proof_of_refund = fields.Binary(string='Proof of Refund Attachment')
    proof_of_refund_filename = fields.Char(string='Proof File Name')

    journal_entry_id = fields.Many2one(
        'account.move', 
        string='Accounting Journal Entry', 
        readonly=True, 
        copy=False
    )

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Refund Remarks & Wire Confirmation Notes')

    @api.depends('original_security_deposit', 'outstanding_rent_deduction', 'damage_deduction', 'utility_deduction', 'other_deduction')
    def _compute_deductions_and_refund(self):
        for rec in self:
            rec.total_deduction = (
                (rec.outstanding_rent_deduction or 0.0) +
                (rec.damage_deduction or 0.0) +
                (rec.utility_deduction or 0.0) +
                (rec.other_deduction or 0.0)
            )
            net = (rec.original_security_deposit or 0.0) - rec.total_deduction
            rec.refundable_amount = max(0.0, net)

    @api.depends('refund_application_date')
    def _compute_expected_release_date(self):
        for rec in self:
            if rec.refund_application_date:
                rec.expected_release_date = rec.refund_application_date + timedelta(days=7)
            else:
                rec.expected_release_date = False

    @api.onchange('move_out_clearance_id')
    def _onchange_move_out_clearance_id(self):
        if self.move_out_clearance_id:
            clearance = self.move_out_clearance_id
            self.tenant_id = clearance.tenant_id
            self.unit_id = clearance.unit_id
            self.lease_contract_id = clearance.lease_contract_id
            self.original_security_deposit = clearance.security_deposit
            self.outstanding_rent_deduction = clearance.outstanding_balance
            self.damage_deduction = clearance.damage_charges
            self.utility_deduction = clearance.utility_charges
            self.other_deduction = clearance.other_deductions

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('security.deposit.refund') or 'REFUND-2026-00001'
        return super(SecurityDepositRefund, self).create(vals)

    def action_submit(self):
        for rec in self:
            if rec.refundable_amount > 0:
                missing = []
                if not rec.bank_name: missing.append("Bank Name")
                if not rec.account_name: missing.append("Account Name")
                if not rec.account_number: missing.append("Account Number")
                if missing:
                    raise UserError(f"Bank Wire Details Incomplete: The following account credentials are required for deposit refund payout: {', '.join(missing)}!")
            rec.finance_approval = 'pending'
            rec.message_post(
                body=f"Security Deposit Refund Application <b>{rec.name}</b> submitted for Tenant <b>{rec.tenant_id.name}</b>. Refundable Amount: PHP {(rec.refundable_amount or 0.0):,.2f}.",
                subject="Refund Application Submitted"
            )

    def action_finance_approve(self):
        for rec in self:
            if rec.refundable_amount > 0:
                missing = []
                if not rec.bank_name: missing.append("Bank Name")
                if not rec.account_name: missing.append("Account Name")
                if not rec.account_number: missing.append("Account Number")
                if missing:
                    raise UserError(f"Finance Approval Blocked: Bank credentials ({', '.join(missing)}) are required before approving payout!")

            # Accounting Treatment: Create Miscellaneous Entry clearing Liability
            if not rec.journal_entry_id:
                misc_journal = self.env['account.journal'].search([('type', '=', 'general')], limit=1)
                entry_vals = {
                    'move_type': 'entry',
                    'journal_id': misc_journal.id if misc_journal else False,
                    'date': fields.Date.context_today(self),
                    'ref': f"Security Deposit Refund & Settlement: {rec.name} [Lease: {rec.lease_contract_id.name}]",
                    'line_ids': [
                        (0, 0, {
                            'name': f"Security Deposit Liability Settlement - Tenant: {rec.tenant_id.name}",
                            'debit': rec.original_security_deposit or 0.0,
                            'credit': 0.0,
                            'partner_id': rec.tenant_id.id,
                        }),
                        (0, 0, {
                            'name': f"Deposit Payout / Deductions Credit - Unit: {rec.unit_id.name}",
                            'debit': 0.0,
                            'credit': rec.original_security_deposit or 0.0,
                            'partner_id': rec.tenant_id.id,
                        }),
                    ]
                }
                entry = self.env['account.move'].create(entry_vals)
                rec.journal_entry_id = entry.id

            rec.finance_approval = 'approved'
            rec.payment_status = 'in_payment'
            rec.message_post(
                body=f"Finance Approval Granted for Refund Claim <b>{rec.name}</b>. Accounting Journal Entry <b>{rec.journal_entry_id.name or 'Draft Entry'}</b> generated. Expected Wire Date: <b>{rec.expected_release_date}</b>.",
                subject="Finance Approval Granted"
            )

    def action_mark_paid(self):
        for rec in self:
            if rec.refundable_amount > 0 and not rec.proof_of_refund:
                raise UserError("Proof of Refund Required: Please attach the electronic bank wire receipt / proof of refund before marking as Paid!")

            rec.payment_status = 'paid'
            if rec.lease_contract_id:
                rec.lease_contract_id.stage = 'deposit_refund'
            rec.message_post(
                body=f"💰 <b>SECURITY DEPOSIT REFUND COMPLETED</b> for Tenant <b>{rec.tenant_id.name}</b>. Net Refund Payout: PHP {(rec.refundable_amount or 0.0):,.2f}.",
                subject="Refund Payment Completed"
            )

    def action_view_journal_entry(self):
        self.ensure_one()
        if not self.journal_entry_id:
            raise UserError("No accounting journal entry generated for this refund claim yet.")
        return {
            'name': 'Accounting Journal Entry',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.journal_entry_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
