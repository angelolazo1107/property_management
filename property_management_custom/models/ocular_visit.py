# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OcularVisit(models.Model):
    _name = 'ocular.visit'
    _description = 'Ocular Visit & Security Gate Pass Coordination'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Ocular Visit Ref', required=True, copy=False, readonly=True, default='New')
    lead_id = fields.Many2one('crm.lead', string='Lead / Opportunity', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Client / Tenant', related='lead_id.partner_id', store=True)
    
    visitor_name = fields.Char(string='Visitor Name', required=True)
    contact_number = fields.Char(string='Contact Number', required=True)
    visit_datetime = fields.Datetime(string='Entry Date and Time', required=True, tracking=True)
    agent_id = fields.Many2one('res.users', string='Contact Person / Agent', default=lambda self: self.env.user, required=True)
    
    building_name = fields.Char(string='Property / Building Name')
    floor_level = fields.Char(string='Floor Level')
    unit_ids = fields.Many2many('product.product', string='Unit/s for Viewing', domain="[('is_property_unit', '=', True)]")
    
    purpose = fields.Selection([
        ('ocular', 'Ocular Visit / Initial Tour'),
        ('inspection', 'Pre-Lease Inspection'),
        ('revisit', 'Client Re-Visit'),
        ('other', 'Other Purpose'),
    ], string='Purpose of Visit', default='ocular', required=True)

    vehicle_type = fields.Selection([
        ('none', 'None / Walk-in'),
        ('car', 'Car / Sedan / SUV'),
        ('motorcycle', 'Motorcycle'),
    ], string='Vehicle Type', default='none', required=True)

    plate_number = fields.Char(string='Vehicle Plate Number')
    parking_required = fields.Boolean(string='Parking Slot Required', default=False)
    
    security_status = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Sent to Security GC'),
        ('confirmed', 'Confirmed by Security'),
    ], string='Security Notification Status', default='draft', tracking=True)

    status = fields.Selection([
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('no_show', 'No Show'),
        ('cancelled', 'Cancelled'),
    ], string='Visit Status', default='scheduled', tracking=True)

    feedback = fields.Text(string='Client Feedback & Post-Tour Notes')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('ocular.visit') or 'OV-00001'
        return super(OcularVisit, self).create(vals)

    def action_send_security(self):
        for rec in self:
            rec.security_status = 'sent'

    def action_confirm_security(self):
        for rec in self:
            rec.security_status = 'confirmed'

    def action_complete_visit(self):
        for rec in self:
            rec.status = 'completed'
            if rec.lead_id:
                rec.lead_id.ocular_status = 'completed'

    def action_no_show(self):
        for rec in self:
            rec.status = 'no_show'

    def action_cancel_visit(self):
        for rec in self:
            rec.status = 'cancelled'
            if rec.lead_id:
                rec.lead_id.ocular_status = 'cancelled'
