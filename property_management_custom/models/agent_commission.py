# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AgentCommission(models.Model):
    _name = 'agent.commission'
    _description = 'Agent Commission Application & Payout'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Claim Reference', 
        required=True, 
        copy=False, 
        readonly=True, 
        default='New'
    )
    tenant_id = fields.Many2one(
        'res.partner', 
        string='Tenant', 
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
    agent_id = fields.Many2one(
        'res.partner', 
        string='Agent / Broker Vendor', 
        required=True, 
        tracking=True
    )
    agent_type = fields.Selection([
        ('internal', 'Internal / In-House Agent'),
        ('outside', 'Outside Agent / Broker'),
    ], string='Agent Type', required=True, default='outside', tracking=True)

    commission_basis = fields.Selection([
        ('one_month', 'One Month Rental'),
        ('percentage', 'Percentage of Rent'),
        ('fixed', 'Fixed Amount'),
    ], string='Commission Basis', required=True, default='one_month', tracking=True)

    commission_percentage = fields.Float(
        string='Commission Percentage (%)', 
        default=100.0, 
        tracking=True
    )
    commission_amount = fields.Monetary(
        string='Commission Amount (PHP)', 
        currency_field='currency_id', 
        compute='_compute_commission_amount', 
        store=True, 
        readonly=False, 
        tracking=True
    )

    agent_bank_name = fields.Char(string='Agent Bank Name', tracking=True)
    agent_bank_account_name = fields.Char(string='Agent Bank Account Name', tracking=True)
    agent_bank_account_number = fields.Char(string='Agent Bank Account Number', tracking=True)

    agent_valid_id = fields.Binary(string='Agent Valid ID Attachment')
    agent_valid_id_filename = fields.Char(string='Valid ID File Name')

    contract_signed = fields.Boolean(
        string='Contract Signed?', 
        compute='_compute_contract_and_move_in_status', 
        store=True, 
        tracking=True
    )
    move_in_completed = fields.Boolean(
        string='Move-In Completed?', 
        compute='_compute_contract_and_move_in_status', 
        store=True, 
        tracking=True
    )

    approval_status = fields.Selection([
        ('draft', 'Draft Claim'),
        ('for_leasing_approval', 'For Leasing Approval'),
        ('for_finance_approval', 'For Finance Approval'),
        ('approved', 'Approved for Payout'),
        ('paid', 'Paid'),
        ('rejected', 'Rejected'),
    ], string='Approval Status', default='draft', tracking=True)

    vendor_bill_id = fields.Many2one(
        'account.move', 
        string='Vendor Bill (Accounting)', 
        readonly=True, 
        copy=False
    )
    vendor_bill_payment_state = fields.Selection(
        related='vendor_bill_id.payment_state', 
        string='Vendor Bill Payment Status'
    )

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Notes / Bank Wire Instructions')

    @api.depends('lease_contract_id', 'lease_contract_id.stage', 'lease_contract_id.tenant_signed', 'lease_contract_id.move_in_cleared')
    def _compute_contract_and_move_in_status(self):
        signed_stages = ['signed_tenant', 'submitted_billing', 'submitted_legal', 'for_notarization', 'notarized', 'released_tenant', 'active']
        for rec in self:
            if rec.lease_contract_id:
                rec.contract_signed = (rec.lease_contract_id.stage in signed_stages) or bool(rec.lease_contract_id.tenant_signed)
                rec.move_in_completed = bool(rec.lease_contract_id.move_in_cleared) or (rec.lease_contract_id.stage == 'active')
            else:
                rec.contract_signed = False
                rec.move_in_completed = False

    @api.depends('commission_basis', 'commission_percentage', 'lease_contract_id', 'lease_contract_id.monthly_rent')
    def _compute_commission_amount(self):
        for rec in self:
            monthly_rent = rec.lease_contract_id.monthly_rent if rec.lease_contract_id else 0.0
            if rec.commission_basis == 'one_month':
                rec.commission_amount = monthly_rent
            elif rec.commission_basis == 'percentage':
                rec.commission_amount = (monthly_rent or 0.0) * ((rec.commission_percentage or 0.0) / 100.0)
            elif rec.commission_basis == 'fixed':
                if not rec.commission_amount:
                    rec.commission_amount = monthly_rent

    @api.onchange('lease_contract_id')
    def _onchange_lease_contract_id(self):
        if self.lease_contract_id:
            self.tenant_id = self.lease_contract_id.tenant_id
            self.unit_id = self.lease_contract_id.unit_id

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('agent.commission') or 'COMM-2026-00001'
        return super(AgentCommission, self).create(vals_list)

    def action_submit(self):
        for rec in self:
            missing = []
            if not rec.agent_bank_name:
                missing.append("Agent Bank Name")
            if not rec.agent_bank_account_name:
                missing.append("Agent Bank Account Name")
            if not rec.agent_bank_account_number:
                missing.append("Agent Bank Account Number")
            if not rec.agent_valid_id:
                missing.append("Agent Valid ID Attachment")

            if missing:
                raise UserError(f"Payout Credentials Incomplete: The following bank and identity details are required before submitting commission claim: {', '.join(missing)}!")

            rec.approval_status = 'for_leasing_approval'
            rec.message_post(
                body=f"Agent Commission Claim <b>{rec.name}</b> submitted for Agent <b>{rec.agent_id.name}</b> (Amount: PHP {(rec.commission_amount or 0.0):,.2f}). Bank: {rec.agent_bank_name} ({rec.agent_bank_account_number}).",
                subject="Commission Claim Submitted"
            )

    def action_leasing_approve(self):
        for rec in self:
            if not rec.contract_signed:
                raise UserError("Leasing Approval Blocked: Commission claim requires a verified signed Lease Contract!")
            rec.approval_status = 'for_finance_approval'
            rec.message_post(
                body=f"Commission Claim <b>{rec.name}</b> Approved by Leasing Department. Forwarded to Finance for Vendor Bill Creation & Payout.",
                subject="Leasing Approval Granted"
            )

    def action_finance_approve(self):
        for rec in self:
            if not rec.contract_signed:
                raise UserError("Finance Approval Blocked: Contract must be signed prior to commission payout!")

            # 1. Ensure Agent partner is flagged as Supplier / Vendor
            if rec.agent_id and hasattr(rec.agent_id, 'supplier_rank'):
                rec.agent_id.supplier_rank = max(rec.agent_id.supplier_rank or 0, 1)

            # 2. Auto-create Vendor Bill in Accounting
            if not rec.vendor_bill_id:
                bill_vals = {
                    'move_type': 'in_invoice',
                    'partner_id': rec.agent_id.id,
                    'invoice_date': fields.Date.context_today(self),
                    'ref': f"Agent Commission Claim: {rec.name} [Lease: {rec.lease_contract_id.name}]",
                    'invoice_line_ids': [(0, 0, {
                        'name': f"Agent Commission ({rec.agent_type.title()}) - Tenant: {rec.tenant_id.name} [Unit: {rec.unit_id.name}]",
                        'quantity': 1,
                        'price_unit': rec.commission_amount or 0.0,
                    })],
                }
                bill = self.env['account.move'].create(bill_vals)
                rec.vendor_bill_id = bill.id

            rec.approval_status = 'approved'
            rec.message_post(
                body=f"Commission Claim <b>{rec.name}</b> Approved by Finance. Accounting Vendor Bill <b>{rec.vendor_bill_id.name or 'Draft Bill'}</b> generated for PHP {(rec.commission_amount or 0.0):,.2f}.",
                subject="Finance Approval & Vendor Bill Created"
            )

    def action_reject(self):
        for rec in self:
            rec.approval_status = 'rejected'
            rec.message_post(
                body=f"Commission Claim <b>{rec.name}</b> was Rejected by Management.",
                subject="Commission Claim Rejected"
            )

    def action_view_vendor_bill(self):
        self.ensure_one()
        if not self.vendor_bill_id:
            raise UserError("No Vendor Bill generated for this commission claim yet.")
        return {
            'name': 'Accounting Vendor Bill',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.vendor_bill_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
