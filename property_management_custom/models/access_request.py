# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class AccessRequest(models.Model):
    _name = 'access.request'
    _description = 'Access Card / Biometrics Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Request Reference', 
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
    access_type = fields.Selection([
        ('biometrics', 'Biometrics'),
        ('access_card', 'Access Card'),
    ], string='Access Type', required=True, default='biometrics', tracking=True)

    number_of_cards = fields.Integer(
        string='Number of Cards', 
        default=1, 
        tracking=True
    )
    valid_id = fields.Binary(string='Valid ID Attachment')
    valid_id_filename = fields.Char(string='Valid ID File Name')

    unit_price = fields.Monetary(
        string='Unit Price per Card', 
        currency_field='currency_id', 
        default=300.0
    )
    fee = fields.Monetary(
        string='Fee (PHP)', 
        currency_field='currency_id', 
        compute='_compute_fee', 
        store=True, 
        readonly=False, 
        tracking=True
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
    invoice_payment_state = fields.Char(
        string='Invoice Payment Status', 
        related='invoice_id.payment_state', 
        store=True
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('for_payment', 'For Payment'),
        ('for_processing', 'For Processing'),
        ('completed', 'Completed'),
        ('released', 'Released'),
    ], string='Request Status', default='draft', tracking=True)

    released_card_number = fields.Char(
        string='Released Card Number(s)', 
        tracking=True, 
        help="Record the physical card number(s) released by Security/Admin."
    )
    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id
    )
    notes = fields.Text(string='Notes / Remarks')

    @api.depends('access_type', 'number_of_cards', 'unit_price')
    def _compute_fee(self):
        for rec in self:
            if rec.access_type == 'access_card':
                num_cards = rec.number_of_cards if rec.number_of_cards > 0 else 1
                rec.fee = num_cards * (rec.unit_price or 300.0)
            else:
                rec.fee = 0.0

    @api.onchange('access_type')
    def _onchange_access_type(self):
        if self.access_type == 'biometrics':
            self.fee = 0.0
            self.payment_status = 'waived'
        else:
            if self.payment_status == 'waived' and not self.cashier_receipt:
                self.payment_status = 'unpaid'
            self._compute_fee()

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('access.request') or 'ACR-2026-00001'
        return super(AccessRequest, self).create(vals)

    def action_submit(self):
        for rec in self:
            if rec.access_type == 'biometrics':
                rec.fee = 0.0
                rec.payment_status = 'waived'
                rec.state = 'for_processing'
                rec.message_post(
                    body=f"Biometrics Request <b>{rec.name}</b> submitted (Free of charge). Advanced to For Processing.",
                    subject="Biometrics Request Submitted"
                )
            else:
                if rec.number_of_cards <= 0:
                    raise UserError("Number of Cards must be greater than 0 for Access Card requests!")
                rec._compute_fee()
                rec.payment_status = 'unpaid'
                rec.state = 'for_payment'

                # Auto-create invoice if not already created
                if not rec.invoice_id:
                    invoice_vals = {
                        'move_type': 'out_invoice',
                        'partner_id': rec.tenant_id.id,
                        'invoice_date': fields.Date.context_today(self),
                        'ref': f"Access Card Application: {rec.name}",
                        'invoice_line_ids': [(0, 0, {
                            'name': f"Access Card Fee - {rec.number_of_cards} Card(s) [Unit: {rec.unit_id.name}]",
                            'quantity': rec.number_of_cards,
                            'price_unit': rec.unit_price or 300.0,
                        })],
                    }
                    invoice = self.env['account.move'].create(invoice_vals)
                    rec.invoice_id = invoice.id

                rec.message_post(
                    body=f"Access Card Request <b>{rec.name}</b> submitted for {rec.number_of_cards} card(s). Invoice <b>{rec.invoice_id.name or 'Draft Invoice'}</b> created for PHP {(rec.fee or 0.0):,.2f}.",
                    subject="Access Card Request & Invoice Created"
                )

    def action_validate_payment(self):
        for rec in self:
            rec.payment_status = 'paid'
            if rec.state in ['draft', 'for_payment']:
                rec.state = 'for_processing'
            rec.message_post(
                body=f"Payment of PHP {(rec.fee or 0.0):,.2f} for Access Request <b>{rec.name}</b> confirmed by Cashier. Advanced to For Processing.",
                subject="Payment Validated"
            )

    def action_waive_payment(self):
        for rec in self:
            rec.payment_status = 'waived'
            if rec.state in ['draft', 'for_payment']:
                rec.state = 'for_processing'
            rec.message_post(
                body=f"Fee for Access Request <b>{rec.name}</b> waived by Admin. Advanced to For Processing.",
                subject="Payment Waived"
            )

    def action_process(self):
        for rec in self:
            rec.state = 'for_processing'

    def action_complete(self):
        for rec in self:
            rec.state = 'completed'

    def action_release_card(self):
        for rec in self:
            if rec.access_type == 'access_card':
                if rec.payment_status not in ['paid', 'waived']:
                    raise UserError("Cannot release card: Payment status is Unpaid! Cashier must validate payment before Security/Admin can release access cards.")
                if not rec.released_card_number:
                    raise UserError("Please record the Released Card Number(s) before completing the release!")
            
            rec.state = 'released'
            rec.message_post(
                body=f"Access Request <b>{rec.name}</b> marked as Released/Completed. Card Number(s): <b>{rec.released_card_number or 'N/A (Biometrics)'}</b>.",
                subject="Access Granted / Card Released"
            )

    def action_view_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            raise UserError("No invoice has been generated for this access request yet.")
        return {
            'name': 'Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
