# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PMOInspection(models.Model):
    _name = 'pmo.inspection'
    _description = 'PMO Move-In and Move-Out Inspection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Inspection Number', required=True, copy=False, readonly=True, default='New')
    unit_id = fields.Many2one('property.unit', string='Property Unit', required=True, tracking=True)
    tenant_id = fields.Many2one('res.partner', string='Tenant Name')
    lease_contract_id = fields.Many2one('lease.contract', string='Lease Contract Reference')

    inspection_type = fields.Selection([
        ('move_in', 'Move-In Baseline Inspection'),
        ('move_out', 'Move-Out Turnover Assessment'),
        ('routine', 'Routine PMO Maintenance Inspection'),
    ], string='Inspection Category', default='move_in', required=True, tracking=True)
    
    inspection_date = fields.Datetime(string='Inspection Timestamp', default=fields.Datetime.now, required=True)
    inspector_id = fields.Many2one('res.users', string='PMO Inspector', default=lambda self: self.env.user, required=True)
    
    electric_reading = fields.Float(string='Electricity Reading (kWh)', required=True)
    water_reading = fields.Float(string='Water Reading (cbm)', required=True)
    
    access_cards_issued = fields.Integer(string='Access Cards / Keys Count Issued')
    access_cards_returned = fields.Integer(string='Access Cards / Keys Count Returned')

    unit_condition = fields.Selection([
        ('pass', 'Passed - Pristine Condition'),
        ('minor_repairs', 'Conditional - Minor Repairs Required'),
        ('major_damage', 'Failed - Major Damage / Missing Items'),
    ], string='Condition Assessment', default='pass', tracking=True)
    
    chargeable_findings = fields.Text(string='Chargeable Findings & Damage List')
    tenant_signature = fields.Binary(string='Tenant Acknowledgment Signature')
    
    info_desk_verified = fields.Boolean(string='Info Desk Recording Verified')
    security_coordination = fields.Boolean(string='Security Coordination Cleared')
    wifi_parking_assigned = fields.Boolean(string='Parking / Access / Wi-Fi Assigned')

    
    status = fields.Selection([
        ('draft', 'Inspection Draft'),
        ('submitted', 'Submitted to PMO'),
        ('verified', 'Accounting & PMO Verified'),
    ], string='Inspection Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('pmo.inspection') or 'INSP-0001'
        return super(PMOInspection, self).create(vals)

    def action_verify_inspection(self):
        for rec in self:
            rec.status = 'verified'
            # Sync baseline meter readings back to Unit
            if rec.unit_id:
                rec.unit_id.latest_electric_reading = rec.electric_reading
                rec.unit_id.latest_water_reading = rec.water_reading
