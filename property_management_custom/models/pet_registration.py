# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class PetRegistration(models.Model):
    _name = 'pet.registration'
    _description = 'Pet Registration & Permit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Registration Ref', 
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
    move_in_form_id = fields.Many2one(
        'move.in.form', 
        string='Move-In Form Reference',
        ondelete='cascade'
    )

    pet_type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('other', 'Other'),
    ], string='Pet Type', required=True, default='dog', tracking=True)

    pet_name = fields.Char(string='Pet Name', tracking=True)
    breed = fields.Char(string='Breed / Species', tracking=True)

    registration_fee = fields.Monetary(
        string='Registration Fee (PHP)', 
        currency_field='currency_id', 
        default=500.0, 
        tracking=True
    )
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('waived', 'Waived'),
    ], string='Payment Status', default='unpaid', tracking=True)

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

    pet_photo = fields.Binary(string='Pet Photo')
    pet_photo_filename = fields.Char(string='Pet Photo File Name')

    vaccination_record = fields.Binary(string='Vaccination Record Attachment')
    vaccination_record_filename = fields.Char(string='Vaccination File Name')

    state = fields.Selection([
        ('draft', 'Draft Permit'),
        ('active', 'Active Permit'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Behavioral & Health Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('pet.registration') or 'PET-2026-00001'
        return super(PetRegistration, self).create(vals_list)

    def action_submit(self):
        for rec in self:
            rec.payment_status = 'unpaid'
            if not rec.invoice_id:
                p_type_label = dict(rec._fields['pet_type'].selection).get(rec.pet_type)
                invoice_vals = {
                    'move_type': 'out_invoice',
                    'partner_id': rec.tenant_id.id,
                    'invoice_date': fields.Date.context_today(self),
                    'ref': f"Pet Registration Fee: {rec.name} ({rec.pet_name or 'Pet'})",
                    'invoice_line_ids': [(0, 0, {
                        'name': f"Pet Registration Fee ({p_type_label}: {rec.pet_name or 'Unnamed'}) - Unit: {rec.unit_id.name}",
                        'quantity': 1,
                        'price_unit': rec.registration_fee or 500.0,
                    })],
                }
                invoice = self.env['account.move'].create(invoice_vals)
                rec.invoice_id = invoice.id

            rec.message_post(
                body=f"Pet Registration <b>{rec.name}</b> submitted for {rec.pet_name or 'Pet'} ({rec.pet_type}). Customer Invoice <b>{rec.invoice_id.name or 'Draft Invoice'}</b> created for PHP {(rec.registration_fee or 500.0):,.2f}.",
                subject="Pet Registration Submitted"
            )

    def action_validate_payment(self):
        for rec in self:
            rec.payment_status = 'paid'
            rec.state = 'active'
            rec.message_post(
                body=f"Pet Registration Fee of PHP {(rec.registration_fee or 500.0):,.2f} for <b>{rec.pet_name or 'Pet'}</b> ({rec.name}) confirmed by Cashier. Permit Activated.",
                subject="Pet Registration Payment Confirmed"
            )

    def action_waive_payment(self):
        for rec in self:
            rec.payment_status = 'waived'
            rec.state = 'active'
            rec.message_post(
                body=f"Pet Registration Fee for <b>{rec.pet_name or 'Pet'}</b> ({rec.name}) waived by Admin. Permit Activated.",
                subject="Pet Fee Waived"
            )

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
            rec.message_post(body=f"Pet Permit <b>{rec.name}</b> cancelled.", subject="Pet Permit Cancelled")

    def action_view_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            raise UserError("No customer invoice generated for this pet registration yet.")
        return {
            'name': 'Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
