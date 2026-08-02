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
    
    # Stage 2 Ocular Visit Integration
    ocular_visit_ids = fields.One2many('ocular.visit', 'lead_id', string='Ocular Visit Records')
    ocular_visit_count = fields.Integer(string='Ocular Visits Count', compute='_compute_ocular_visit_count')

    ocular_visit_date = fields.Datetime(string='Next Ocular Visit Schedule')
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

    @api.depends('ocular_visit_ids')
    def _compute_ocular_visit_count(self):
        for rec in self:
            rec.ocular_visit_count = len(rec.ocular_visit_ids)

    def action_view_ocular_visits(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_ocular_visit")
        action['domain'] = [('lead_id', '=', self.id)]
        action['context'] = {
            'default_lead_id': self.id,
            'default_visitor_name': self.contact_name or self.partner_name or self.name,
            'default_contact_number': self.phone or self.mobile,
            'default_agent_id': self.user_id.id if self.user_id else self.env.uid,
        }
        return action

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
