# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class VisitorGatePass(models.Model):
    _name = 'visitor.gate.pass'
    _description = 'Security Visitor Gate Pass'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Gate Pass Ref', required=True, copy=False, readonly=True, default='New')
    ocular_visit_id = fields.Many2one('ocular.visit', string='Ocular Visit Reference')
    lead_id = fields.Many2one('crm.lead', string='CRM Opportunity', related='ocular_visit_id.lead_id', store=True)
    
    visitor_name = fields.Char(string='Visitor Name', required=True)
    entry_datetime = fields.Datetime(string='Scheduled Entry Date & Time', required=True)
    agent_id = fields.Many2one('res.users', string='Contact Person / Agent', required=True)
    floor_and_unit = fields.Char(string='Floor and Unit/s for Viewing', required=True)
    purpose = fields.Char(string='Purpose of Visit', default='Ocular Visit', required=True)
    vehicle_info = fields.Char(string='Vehicle Information (Car / Motorcycle / Plate No)')
    
    check_in_datetime = fields.Datetime(string='Actual Check-In Time', readonly=True)
    check_out_datetime = fields.Datetime(string='Actual Check-Out Time', readonly=True)

    status = fields.Selection([
        ('pending', 'Pending Review'),
        ('sent', 'Sent to Security GC'),
        ('approved', 'Security Approved'),
        ('checked_in', 'Checked-In at Gate'),
        ('checked_out', 'Checked-Out'),
    ], string='Security Status', default='pending', tracking=True)

    notes = fields.Text(string='Security Gate Notes & Incident Log')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('visitor.gate.pass') or 'GP-00001'
        return super(VisitorGatePass, self).create(vals_list)

    def _validate_gate_pass_requirements(self):
        for rec in self:
            missing = []
            if not rec.visitor_name:
                missing.append("Visitor Name")
            if not rec.entry_datetime:
                missing.append("Entry Time")
            if not rec.agent_id:
                missing.append("Contact Person / Agent")
            if not rec.floor_and_unit:
                missing.append("Floor and Unit Number")
            if not rec.purpose:
                missing.append("Purpose of Visit")
            
            if missing:
                raise UserError(f"Gate Pass Validation Error: Before confirming or sending to Security, the following fields are required: {', '.join(missing)}.")

    def action_send_security(self):
        for rec in self:
            rec._validate_gate_pass_requirements()
            rec.status = 'sent'

    def action_approve_security(self):
        for rec in self:
            rec._validate_gate_pass_requirements()
            rec.status = 'approved'

    def action_check_in(self):
        for rec in self:
            rec.status = 'checked_in'
            rec.check_in_datetime = fields.Datetime.now()

    def action_check_out(self):
        for rec in self:
            rec.status = 'checked_out'
            rec.check_out_datetime = fields.Datetime.now()
