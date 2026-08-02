# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    target_unit_id = fields.Many2one('product.product', string='Target Unit / Property', domain="[('is_property_unit', '=', True)]")
    intended_move_in_date = fields.Date(string='Intended Move-In Date')
    preferred_budget = fields.Monetary(string='Preferred Rent Budget', currency_field='company_currency')
    
    parking_required = fields.Boolean(string='Parking Requirement')
    wifi_required = fields.Boolean(string='Wi-Fi Connection Requirement')
    pet_details = fields.Char(string='Pet Details / Registration')
    broker_id = fields.Many2one('res.partner', string='Assigned Broker / Agent')
    
    ocular_visit_date = fields.Datetime(string='Ocular Visit Schedule')
    security_visitor_details = fields.Text(string='Visitor Security Details (For Gate Pass)')
    ocular_status = fields.Selection([
        ('pending', 'Pending Schedule'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Visit Completed'),
        ('rescheduled', 'Rescheduled'),
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
    reservation_verified = fields.Boolean(string='Accounting Verified Payment', tracking=True)
    official_receipt_no = fields.Char(string='Official Receipt (OR) Ref')
    unit_hold_status = fields.Selection([
        ('none', 'No Hold'),
        ('hold_active', 'Unit Blocked / On Hold'),
        ('released', 'Hold Released'),
    ], string='Unit Blocking Status', default='none', tracking=True)

    legal_clearance = fields.Boolean(string='Legal Clearance Approved', tracking=True)
    move_in_cleared = fields.Boolean(string='Move-In Financial Clearance Granted', tracking=True)

    def action_schedule_ocular(self):
        for rec in self:
            rec.ocular_status = 'scheduled'

    def action_complete_ocular(self):
        for rec in self:
            rec.ocular_status = 'completed'

    def action_verify_bis(self):
        for rec in self:
            rec.bis_status = 'verified'

    def action_verify_reservation_payment(self):
        for rec in self:
            rec.reservation_verified = True
            rec.unit_hold_status = 'hold_active'
            if rec.target_unit_id:
                rec.target_unit_id.occupancy_status = 'reserved'

    def action_verify_move_in_clearance(self):
        for rec in self:
            rec.move_in_cleared = True
