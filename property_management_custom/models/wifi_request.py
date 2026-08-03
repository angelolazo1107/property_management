# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class WifiRequest(models.Model):
    _name = 'wifi.request'
    _description = 'Internet / Wi-Fi Application'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Application Ref', 
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
        string='Unit', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    plan_type = fields.Selection([
        ('residential', 'Residential Plan'),
        ('commercial', 'Commercial Plan'),
    ], string='Plan Type', required=True, default='residential', tracking=True)

    monthly_fee = fields.Monetary(
        string='Monthly Plan Fee', 
        currency_field='currency_id', 
        default=1500.0, 
        tracking=True
    )
    installation_fee = fields.Monetary(
        string='Installation Fee', 
        currency_field='currency_id', 
        default=500.0, 
        tracking=True
    )
    total_upfront_fee = fields.Monetary(
        string='Total Upfront Fee', 
        currency_field='currency_id', 
        compute='_compute_total_upfront_fee', 
        store=True
    )

    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('waived', 'Waived'),
    ], string='Payment Status', default='unpaid', tracking=True)

    cashier_receipt = fields.Binary(string='Cashier Receipt / Proof of Payment')
    cashier_receipt_filename = fields.Char(string='Cashier Receipt File Name')
    invoice_id = fields.Many2one(
        'account.move', 
        string='Customer Invoice', 
        readonly=True, 
        copy=False
    )
    invoice_payment_state = fields.Selection(
        related='invoice_id.payment_state', 
        string='Invoice Payment Status'
    )

    helpdesk_ticket_id = fields.Many2one(
        'helpdesk.ticket', 
        string='IT Helpdesk Ticket', 
        readonly=True, 
        copy=False
    )

    installation_schedule = fields.Datetime(
        string='Installation Schedule Date & Time', 
        tracking=True
    )
    wifi_username = fields.Char(
        string='Wi-Fi SSID / Username', 
        tracking=True
    )
    wifi_password = fields.Char(
        string='Wi-Fi Password / Key', 
        tracking=True
    )
    router_serial = fields.Char(
        string='Router / Device Serial Number', 
        tracking=True
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('for_payment', 'For Payment'),
        ('for_it_installation', 'For IT Installation'),
        ('installed', 'Installed'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Notes / Special Instructions')

    @api.depends('monthly_fee', 'installation_fee')
    def _compute_total_upfront_fee(self):
        for rec in self:
            rec.total_upfront_fee = (rec.monthly_fee or 0.0) + (rec.installation_fee or 0.0)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('wifi.request') or 'WIFI-2026-00001'
        return super(WifiRequest, self).create(vals)

    def action_submit(self):
        for rec in self:
            rec._compute_total_upfront_fee()
            rec.payment_status = 'unpaid'
            rec.state = 'for_payment'

            # Auto-create Customer Invoice if not exists
            if not rec.invoice_id:
                invoice_lines = [(0, 0, {
                    'name': f"Internet Subscription ({rec.plan_type.title()} Plan) - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.monthly_fee or 0.0,
                })]
                if (rec.installation_fee or 0.0) > 0:
                    invoice_lines.append((0, 0, {
                        'name': f"Wi-Fi Installation & Hardware Setup Fee - Unit: {rec.unit_id.name}",
                        'quantity': 1,
                        'price_unit': rec.installation_fee or 0.0,
                    }))

                invoice_vals = {
                    'move_type': 'out_invoice',
                    'partner_id': rec.tenant_id.id,
                    'invoice_date': fields.Date.context_today(self),
                    'ref': f"Internet Application: {rec.name}",
                    'invoice_line_ids': invoice_lines,
                }
                invoice = self.env['account.move'].create(invoice_vals)
                rec.invoice_id = invoice.id

            rec.message_post(
                body=f"Internet/Wi-Fi Application <b>{rec.name}</b> submitted. Customer Invoice <b>{rec.invoice_id.name or 'Draft Invoice'}</b> created for PHP {(rec.total_upfront_fee or 0.0):,.2f}.",
                subject="Internet Application Submitted"
            )

    def action_validate_payment(self):
        for rec in self:
            rec.payment_status = 'paid'
            rec.state = 'for_it_installation'

            # Auto-create IT Helpdesk Ticket if not exists
            if not rec.helpdesk_ticket_id:
                ticket_vals = {
                    'name': f"Wi-Fi Installation Request: {rec.name} - Unit {rec.unit_id.name or ''}",
                    'partner_id': rec.tenant_id.id,
                    'description': (
                        f"Tenant: {rec.tenant_id.name}\n"
                        f"Unit: {rec.unit_id.name or ''}\n"
                        f"Plan Type: {dict(rec._fields['plan_type'].selection).get(rec.plan_type)}\n"
                        f"Monthly Fee: PHP {(rec.monthly_fee or 0.0):,.2f}\n"
                        f"Payment Status: Paid (Invoice {rec.invoice_id.name or ''})\n"
                        f"Special Instructions: {rec.notes or 'None'}"
                    ),
                }
                # Assign to IT Helpdesk Team if available
                it_team = self.env['helpdesk.team'].search([('name', 'ilike', 'IT')], limit=1)
                if it_team:
                    ticket_vals['team_id'] = it_team.id

                ticket = self.env['helpdesk.ticket'].create(ticket_vals)
                rec.helpdesk_ticket_id = ticket.id

            rec.message_post(
                body=f"Payment for Internet Application <b>{rec.name}</b> confirmed by Cashier. Advanced to For IT Installation. IT Ticket <b>{rec.helpdesk_ticket_id.name}</b> created & assigned.",
                subject="Payment Confirmed & IT Ticket Dispatched"
            )

    def action_waive_payment(self):
        for rec in self:
            rec.payment_status = 'waived'
            rec.state = 'for_it_installation'
            rec.message_post(
                body=f"Payment for Internet Application <b>{rec.name}</b> waived by Admin. Moved to For IT Installation.",
                subject="Payment Waived"
            )

    def action_mark_installed(self):
        for rec in self:
            if not rec.wifi_username and not rec.router_serial:
                raise UserError("Please enter the Wi-Fi SSID / Username or Router Device Serial Number before completing installation!")

            rec.state = 'installed'

            # Link Wi-Fi Info to Active Lease Contract if present
            lease = self.env['lease.contract'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id),
                ('stage', 'in', ['active', 'released_tenant', 'notarized'])
            ], limit=1)
            if lease:
                lease.wifi_fee = rec.monthly_fee
                lease.message_post(
                    body=f"Wi-Fi Installed for Unit <b>{rec.unit_id.name}</b>. SSID: <b>{rec.wifi_username or 'N/A'}</b> | Router Serial: <b>{rec.router_serial or 'N/A'}</b>. Monthly Wi-Fi Fee set to PHP {(rec.monthly_fee or 0.0):,.2f}.",
                    subject="Wi-Fi Credentials Registered to Lease"
                )

            # Post automated notification to Tenant
            rec.message_post(
                body=(
                    f"Wi-Fi Installation completed for Tenant <b>{rec.tenant_id.name}</b> at Unit <b>{rec.unit_id.name}</b>!<br/>"
                    f"<b>Wi-Fi SSID:</b> {rec.wifi_username or 'N/A'}<br/>"
                    f"<b>Wi-Fi Password:</b> {rec.wifi_password or 'Provided on device'}<br/>"
                    f"<b>Router Serial:</b> {rec.router_serial or 'N/A'}<br/>"
                    f"<b>Installation Schedule:</b> {rec.installation_schedule or 'Completed'}"
                ),
                subject="Wi-Fi Installation Completed - Login Credentials"
            )

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
            rec.message_post(
                body=f"Internet Application <b>{rec.name}</b> has been cancelled.",
                subject="Application Cancelled"
            )

    def action_view_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            raise UserError("No invoice has been generated for this request yet.")
        return {
            'name': 'Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_view_helpdesk_ticket(self):
        self.ensure_one()
        if not self.helpdesk_ticket_id:
            raise UserError("No IT Helpdesk ticket has been generated for this request yet.")
        return {
            'name': 'IT Helpdesk Ticket',
            'type': 'ir.actions.act_window',
            'res_model': 'helpdesk.ticket',
            'res_id': self.helpdesk_ticket_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
