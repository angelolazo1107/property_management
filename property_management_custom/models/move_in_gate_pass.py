# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MoveInGatePass(models.Model):
    _name = 'move.in.gate.pass'
    _description = 'Move-In Gate Pass & Security Control'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Gate Pass Ref', 
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
    move_in_date = fields.Date(
        string='Move-In Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )

    vehicle_details = fields.Char(
        string='Vehicle Details', 
        tracking=True, 
        help="Specify vehicle make, model, color, and plate number (e.g. Toyota HiAce White - Plate ABC 1234)."
    )
    items_for_move_in = fields.Text(
        string='Items for Move-In', 
        help="List of furniture, appliances, boxes, and personal belongings allowed entry."
    )

    prepared_by_id = fields.Many2one(
        'res.users', 
        string='Prepared By (Leasing/Admin)', 
        default=lambda self: self.env.user, 
        tracking=True
    )
    submitted_to_security = fields.Boolean(
        string='Submitted to Security', 
        default=False, 
        tracking=True
    )

    security_status = fields.Selection([
        ('pending', 'Pending Approval'),
        ('sent', 'Sent to Security'),
        ('approved', 'Approved by Security'),
        ('used', 'Gate Pass Used / Move-In Complete'),
    ], string='Security Status', default='pending', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Security Inspection Remarks')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('move.in.gate.pass') or 'MGP-2026-00001'
        return super(MoveInGatePass, self).create(vals)

    def action_submit_security(self):
        for rec in self:
            rec.submitted_to_security = True
            rec.security_status = 'sent'
            rec.message_post(
                body=f"Move-In Gate Pass <b>{rec.name}</b> for Tenant <b>{rec.tenant_id.name}</b> on Unit <b>{rec.unit_id.name}</b> submitted to Security. Vehicle: {rec.vehicle_details or 'N/A'}.",
                subject="Gate Pass Submitted to Security"
            )

    def action_security_approve(self):
        for rec in self:
            rec.security_status = 'approved'
            rec.message_post(
                body=f"Move-In Gate Pass <b>{rec.name}</b> APPROVED by Security for Move-In Date <b>{rec.move_in_date}</b>.",
                subject="Gate Pass Approved by Security"
            )

    def action_mark_used(self):
        for rec in self:
            rec.security_status = 'used'
            rec.message_post(
                body=f"Move-In Gate Pass <b>{rec.name}</b> MARKED AS USED. Vehicle entry & move-in items cleared by Security.",
                subject="Gate Pass Used"
            )
