# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import date

class RecurringMonthlyBilling(models.Model):
    _name = 'recurring.monthly.billing'
    _description = 'Monthly Billing & Collection Ledger'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Billing Reference', 
        required=True, 
        copy=False, 
        readonly=True, 
        default='New'
    )
    lease_contract_id = fields.Many2one(
        'lease.contract', 
        string='Lease Contract Reference', 
        required=True, 
        tracking=True
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
    billing_cycle_date = fields.Date(
        string='Billing Month / Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )
    billing_day = fields.Selection([
        ('1', 'Every 1st of Month'),
        ('5', 'Every 5th of Month'),
        ('10', 'Every 10th of Month'),
        ('15', 'Every 15th of Month'),
        ('30', 'End of Month'),
    ], string='Billing Day', default='5', tracking=True)

    monthly_rent = fields.Monetary(string='Monthly Rent', currency_field='currency_id', tracking=True)
    furniture_rent = fields.Monetary(string='Furniture Rent', currency_field='currency_id', tracking=True)
    parking_fee = fields.Monetary(string='Parking Fee', currency_field='currency_id', tracking=True)
    wifi_fee = fields.Monetary(string='Wi-Fi Fee', currency_field='currency_id', tracking=True)
    other_recurring_charges = fields.Monetary(string='Other Recurring Charges', currency_field='currency_id', tracking=True)

    total_monthly_billing = fields.Monetary(
        string='Total Monthly Billing', 
        currency_field='currency_id', 
        compute='_compute_total_billing', 
        store=True, 
        tracking=True
    )

    invoice_id = fields.Many2one(
        'account.move', 
        string='Customer Invoice', 
        readonly=True, 
        copy=False
    )
    invoice_status = fields.Selection([
        ('draft', 'Draft Invoice'),
        ('posted', 'Posted'),
        ('sent', 'Sent to Tenant'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
    ], string='Invoice Status', compute='_compute_invoice_status', store=True, tracking=True)

    collection_status = fields.Selection([
        ('current', 'Current / Up to Date'),
        ('due', 'Due for Payment'),
        ('overdue', 'Overdue'),
        ('for_followup', 'For Follow-Up / Escalated'),
    ], string='Collection Status', default='current', tracking=True)

    overdue_days = fields.Integer(
        string='Overdue Days', 
        compute='_compute_overdue_days', 
        store=True
    )
    last_reminder_date = fields.Datetime(string='Last Follow-Up Reminder Sent', readonly=True)

    escalation_level = fields.Selection([
        ('none', 'Normal / Current'),
        ('level_1', '1st Reminder (3 Days Overdue)'),
        ('level_2', 'Manager Escalation (7 Days Overdue)'),
        ('level_3', 'Legal & Management Escalation (15 Days Overdue)'),
    ], string='Escalation Level', default='none', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Billing Remarks')

    @api.depends('monthly_rent', 'furniture_rent', 'parking_fee', 'wifi_fee', 'other_recurring_charges')
    def _compute_total_billing(self):
        for rec in self:
            rec.total_monthly_billing = (
                (rec.monthly_rent or 0.0) +
                (rec.furniture_rent or 0.0) +
                (rec.parking_fee or 0.0) +
                (rec.wifi_fee or 0.0) +
                (rec.other_recurring_charges or 0.0)
            )

    @api.depends('invoice_id', 'invoice_id.state', 'invoice_id.payment_state', 'overdue_days')
    def _compute_invoice_status(self):
        for rec in self:
            if not rec.invoice_id:
                rec.invoice_status = 'draft'
            elif rec.invoice_id.payment_state in ['paid', 'in_payment']:
                rec.invoice_status = 'paid'
                rec.collection_status = 'current'
            elif rec.overdue_days > 0 and rec.invoice_id.payment_state not in ['paid', 'in_payment']:
                rec.invoice_status = 'overdue'
            elif rec.invoice_id.state == 'posted':
                rec.invoice_status = 'posted'
            else:
                rec.invoice_status = 'draft'

    @api.depends('invoice_id', 'invoice_id.invoice_date_due', 'invoice_id.payment_state')
    def _compute_overdue_days(self):
        today = fields.Date.context_today(self)
        for rec in self:
            if rec.invoice_id and rec.invoice_id.invoice_date_due and rec.invoice_id.payment_state not in ['paid', 'in_payment']:
                due_date = rec.invoice_id.invoice_date_due
                if today > due_date:
                    rec.overdue_days = (today - due_date).days
                else:
                    rec.overdue_days = 0
            else:
                rec.overdue_days = 0

    @api.onchange('lease_contract_id')
    def _onchange_lease_contract_id(self):
        if self.lease_contract_id:
            self.tenant_id = self.lease_contract_id.tenant_id
            self.unit_id = self.lease_contract_id.unit_id
            self.monthly_rent = self.lease_contract_id.monthly_rent
            self.furniture_rent = self.lease_contract_id.furniture_rental_fee
            self.parking_fee = self.lease_contract_id.parking_fee
            self.wifi_fee = self.lease_contract_id.wifi_fee
            self.other_recurring_charges = (self.lease_contract_id.pet_registration_fee or 0.0) + (self.lease_contract_id.other_charges or 0.0)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('recurring.monthly.billing') or 'BILL-2026-08-00001'
        return super(RecurringMonthlyBilling, self).create(vals)

    def action_generate_invoice(self):
        for rec in self:
            if rec.invoice_id:
                raise UserError(f"Customer Invoice {rec.invoice_id.name} already exists for this monthly billing cycle!")

            invoice_lines = []
            if (rec.monthly_rent or 0.0) > 0:
                invoice_lines.append((0, 0, {'name': f"Monthly Rent - Unit: {rec.unit_id.name}", 'quantity': 1, 'price_unit': rec.monthly_rent}))
            if (rec.furniture_rent or 0.0) > 0:
                invoice_lines.append((0, 0, {'name': f"Furniture Rent - Unit: {rec.unit_id.name}", 'quantity': 1, 'price_unit': rec.furniture_rent}))
            if (rec.parking_fee or 0.0) > 0:
                invoice_lines.append((0, 0, {'name': f"Parking Pass Fee - Unit: {rec.unit_id.name}", 'quantity': 1, 'price_unit': rec.parking_fee}))
            if (rec.wifi_fee or 0.0) > 0:
                invoice_lines.append((0, 0, {'name': f"Internet / Wi-Fi Fee - Unit: {rec.unit_id.name}", 'quantity': 1, 'price_unit': rec.wifi_fee}))
            if (rec.other_recurring_charges or 0.0) > 0:
                invoice_lines.append((0, 0, {'name': f"Other Recurring Charges - Unit: {rec.unit_id.name}", 'quantity': 1, 'price_unit': rec.other_recurring_charges}))

            if not invoice_lines:
                raise UserError("No billable recurring charges found for this billing cycle!")

            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': rec.tenant_id.id,
                'invoice_date': fields.Date.context_today(self),
                'invoice_payment_term_id': rec.tenant_id.property_payment_term_id.id if rec.tenant_id.property_payment_term_id else False,
                'ref': f"Monthly Recurring Billing: {rec.name} [Unit: {rec.unit_id.name}]",
                'invoice_line_ids': invoice_lines,
            }
            invoice = self.env['account.move'].create(invoice_vals)
            rec.invoice_id = invoice.id
            rec.invoice_status = 'draft'

            rec.message_post(
                body=f"Draft Monthly Customer Invoice <b>{invoice.name or 'Draft Invoice'}</b> created for Tenant {rec.tenant_id.name}. Total Amount: PHP {(rec.total_monthly_billing or 0.0):,.2f}.",
                subject="Draft Monthly Invoice Created"
            )

    def action_validate_and_send(self):
        for rec in self:
            if not rec.invoice_id:
                rec.action_generate_invoice()

            if rec.invoice_id.state == 'draft':
                rec.invoice_id.action_post()

            rec.invoice_status = 'sent'
            rec.collection_status = 'due'
            rec.message_post(
                body=f"Monthly Customer Invoice <b>{rec.invoice_id.name}</b> validated and sent to Tenant {rec.tenant_id.name}. Due Date: {rec.invoice_id.invoice_date_due or 'Every 5th'}.",
                subject="Invoice Sent to Tenant"
            )

    def action_run_overdue_escalation(self):
        for rec in self:
            rec._compute_overdue_days()
            days = rec.overdue_days

            if rec.invoice_id and rec.invoice_id.payment_state in ['paid', 'in_payment']:
                rec.collection_status = 'current'
                rec.escalation_level = 'none'
                continue

            if days >= 15:
                rec.escalation_level = 'level_3'
                rec.collection_status = 'overdue'
                rec.last_reminder_date = fields.Datetime.now()
                rec.message_post(
                    body=f"⚠️ <b>LEVEL 3 LEGAL ESCALATION (15+ Days Overdue)</b>: Invoice <b>{rec.invoice_id.name}</b> for Tenant {rec.tenant_id.name} is {days} days overdue. Case escalated to Legal & Executive Management.",
                    subject="Level 3 Legal Escalation"
                )
            elif days >= 7:
                rec.escalation_level = 'level_2'
                rec.collection_status = 'for_followup'
                rec.last_reminder_date = fields.Datetime.now()
                rec.message_post(
                    body=f"🔔 <b>LEVEL 2 MANAGER ESCALATION (7+ Days Overdue)</b>: Invoice <b>{rec.invoice_id.name}</b> is {days} days overdue. Escalated to PMO Billing Manager.",
                    subject="Level 2 Manager Escalation"
                )
            elif days >= 3:
                rec.escalation_level = 'level_1'
                rec.collection_status = 'due'
                rec.last_reminder_date = fields.Datetime.now()
                rec.message_post(
                    body=f"📧 <b>LEVEL 1 OVERDUE REMINDER (3+ Days Overdue)</b>: First Payment Reminder sent to Tenant {rec.tenant_id.name} for Invoice <b>{rec.invoice_id.name}</b>.",
                    subject="Level 1 Payment Reminder Sent"
                )

    @api.model
    def cron_generate_monthly_draft_billings(self):
        """ Runs on 1st of the month: Auto-creates draft monthly billing records for all active lease contracts """
        active_leases = self.env['lease.contract'].search([
            ('stage', 'in', ['active', 'released_tenant', 'notarized'])
        ])
        for lease in active_leases:
            existing = self.search([
                ('lease_contract_id', '=', lease.id),
                ('billing_cycle_date', '>=', date.today().replace(day=1))
            ], limit=1)
            if not existing:
                billing = self.create({
                    'lease_contract_id': lease.id,
                    'tenant_id': lease.tenant_id.id,
                    'unit_id': lease.unit_id.id,
                    'monthly_rent': lease.monthly_rent,
                    'furniture_rent': lease.furniture_rental_fee,
                    'parking_fee': lease.parking_fee,
                    'wifi_fee': lease.wifi_fee,
                    'other_recurring_charges': (lease.pet_registration_fee or 0.0) + (lease.other_charges or 0.0),
                })
                billing.action_generate_invoice()

    @api.model
    def cron_send_monthly_invoices(self):
        """ Runs on 5th of the month: Validates and sends draft monthly customer invoices """
        billings = self.search([
            ('billing_cycle_date', '>=', date.today().replace(day=1)),
            ('invoice_status', '=', 'draft')
        ])
        for billing in billings:
            billing.action_validate_and_send()

    @api.model
    def cron_process_billing_followup(self):
        """ Daily Cron: Audits overdue days and triggers 3-day, 7-day, and 15-day escalation engine """
        billings = self.search([
            ('collection_status', 'in', ['due', 'overdue', 'for_followup']),
            ('invoice_id', '!=', False)
        ])
        for billing in billings:
            billing.action_run_overdue_escalation()

    def action_view_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            raise UserError("No customer invoice generated for this monthly billing cycle yet.")
        return {
            'name': 'Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
