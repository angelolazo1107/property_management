# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    target_unit_id = fields.Many2one('property.unit', string='Target Unit / Property')
    intended_move_in_date = fields.Date(string='Intended Move-In Date')
    
    ocular_visit_date = fields.Datetime(string='Ocular Visit Schedule')
    ocular_status = fields.Selection([
        ('pending', 'Pending Schedule'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Visit Completed'),
        ('cancelled', 'Cancelled'),
    ], string='Ocular Visit Status', default='pending', tracking=True)

    bis_status = fields.Selection([
        ('draft', 'Not Submitted'),
        ('submitted', 'BIS Submitted'),
        ('verified', 'BIS Verified'),
        ('rejected', 'BIS Rejected'),
    ], string='BIS (Tenant Info Sheet)', default='draft', tracking=True)

    reservation_proof = fields.Binary(string='Reservation Deposit Proof')
    reservation_proof_name = fields.Char(string='File Name')
    legal_clearance = fields.Boolean(string='Legal Clearance Approved')

    def action_schedule_ocular(self):
        for rec in self:
            rec.ocular_status = 'scheduled'

    def action_verify_bis(self):
        for rec in self:
            rec.bis_status = 'verified'
