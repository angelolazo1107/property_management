# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class MoveInForm(models.Model):
    _name = 'move.in.form'
    _description = 'PMO Move-In Form & Clearance'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Move-In Ref', 
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
    security_deposit = fields.Monetary(
        string='Security Deposit', 
        currency_field='currency_id', 
        tracking=True
    )
    rental_amount = fields.Monetary(
        string='Rental Amount (Monthly Rent)', 
        currency_field='currency_id', 
        tracking=True
    )
    move_in_date = fields.Date(
        string='Move-In Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )

    tenant_signature = fields.Binary(string='Tenant Signature')
    agent_signature = fields.Binary(string='Agent Signature')

    leasing_officer_id = fields.Many2one(
        'res.users', 
        string='Leasing Officer', 
        default=lambda self: self.env.user, 
        tracking=True
    )
    lease_contract_id = fields.Many2one(
        'lease.contract', 
        string='Lease Contract Reference', 
        tracking=True
    )
    pmo_inspection_id = fields.Many2one(
        'pmo.inspection', 
        string='Move-In Inspection Reference', 
        tracking=True
    )

    pet_registration_ids = fields.One2many(
        'pet.registration', 
        'move_in_form_id', 
        string='Pet Registrations'
    )
    pet_registration_count = fields.Integer(
        string='Pet Registrations Count', 
        compute='_compute_pet_registration_count'
    )

    state = fields.Selection([
        ('draft', 'Draft Form'),
        ('for_approval', 'For Approval'),
        ('cleared', 'Cleared for Move-In'),
        ('moved_in', 'Moved In'),
    ], string='Move-In Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Remarks / Special Instructions')

    @api.depends('pet_registration_ids')
    def _compute_pet_registration_count(self):
        for rec in self:
            rec.pet_registration_count = len(rec.pet_registration_ids)

    @api.onchange('lease_contract_id')
    def _onchange_lease_contract_id(self):
        if self.lease_contract_id:
            self.tenant_id = self.lease_contract_id.tenant_id
            self.unit_id = self.lease_contract_id.unit_id
            self.security_deposit = self.lease_contract_id.security_deposit
            self.rental_amount = self.lease_contract_id.monthly_rent

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('move.in.form') or 'MIF-2026-00001'
        return super(MoveInForm, self).create(vals_list)

    def action_submit(self):
        for rec in self:
            rec.state = 'for_approval'
            rec.message_post(
                body=f"Move-In Form <b>{rec.name}</b> for Tenant {rec.tenant_id.name} on Unit <b>{rec.unit_id.name}</b> submitted for approval.",
                subject="Move-In Form Submitted"
            )

    def action_clear(self):
        for rec in self:
            # B3: Cleared state requires linked contract to be in a signed stage
            signed_stages = [
                'signed_tenant', 'submitted_billing', 'submitted_legal',
                'for_notarization', 'notarized', 'released_tenant', 'active'
            ]
            if rec.lease_contract_id and rec.lease_contract_id.stage not in signed_stages:
                raise UserError(
                    f"Move-In Clearance Blocked: The linked Lease Contract '{rec.lease_contract_id.name}' "
                    f"has not yet been signed by the tenant.\n\n"
                    f"Current Contract Stage: {dict(rec.lease_contract_id._fields['stage'].selection).get(rec.lease_contract_id.stage, '?')}\n\n"
                    f"The tenant must sign the lease contract before move-in clearance can be granted."
                )
            if not rec.tenant_signature:
                raise UserError("Tenant Signature Required: Please ensure the tenant signature is provided on the Move-In Form before clearing.")
            rec.state = 'cleared'
            rec.message_post(
                body=f"Move-In Form <b>{rec.name}</b> Cleared for Move-In. Verified by Leasing Officer {rec.leasing_officer_id.name}.",
                subject="Move-In Form Cleared"
            )

    def action_confirm_moved_in(self):
        for rec in self:
            # B3: Can only confirm moved-in after clearance is granted
            if rec.state != 'cleared':
                raise UserError(
                    f"Move-In Confirmation Blocked: The Move-In Form must be in 'Cleared for Move-In' status before confirming move-in.\n\n"
                    f"Current Status: {dict(rec._fields['state'].selection).get(rec.state, '?')}\n\n"
                    f"Please complete the clearance process (signature, contract verification) first."
                )
            if not rec.tenant_signature:
                raise UserError("Tenant Signature Required: Please capture the tenant signature before marking Moved In.")
            
            rec.state = 'moved_in'
            
            # Update Unit Occupancy
            if rec.unit_id:
                rec.unit_id.occupancy_status = 'occupied'
                rec.unit_id.current_tenant_id = rec.tenant_id

            # Update Lease Contract Stage
            if rec.lease_contract_id:
                rec.lease_contract_id.move_in_cleared = True
                rec.lease_contract_id.stage = 'active'
                rec.lease_contract_id.message_post(
                    body=f"Tenant <b>{rec.tenant_id.name}</b> has officially Moved In via Move-In Form <b>{rec.name}</b> on {rec.move_in_date}.",
                    subject="Tenant Moved In Confirmed"
                )

            rec.message_post(
                body=f"Tenant <b>{rec.tenant_id.name}</b> officially MOVED IN to Unit <b>{rec.unit_id.name}</b> on {rec.move_in_date}. Lease Officer: {rec.leasing_officer_id.name}.",
                subject="Moved In Confirmed"
            )

    def action_view_pet_registrations(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_pet_registration")
        action['domain'] = [('move_in_form_id', '=', self.id)]
        action['context'] = {
            'default_move_in_form_id': self.id,
            'default_tenant_id': self.tenant_id.id if self.tenant_id else False,
            'default_unit_id': self.unit_id.id if self.unit_id else False,
        }
        return action
