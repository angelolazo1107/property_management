# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PMOInspection(models.Model):
    _name = 'pmo.inspection'
    _description = 'PMO Move-In and Move-Out Inspection'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Inspection Number', required=True, copy=False, readonly=True, default='New')
    unit_id = fields.Many2one('product.product', string='Property Unit', domain="[('is_property_unit', '=', True)]", required=True, tracking=True)
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
    
    # Access Item Checklists (Keys, Cards, Remotes, Gate Passes & Stickers)
    keys_count = fields.Integer(string='Keys Count')
    access_cards_count = fields.Integer(string='Access Cards Count')
    remotes_count = fields.Integer(string='Aircon / Gate Remote Count')
    gate_passes_count = fields.Integer(string='Gate Pass Issued Count')
    stickers_count = fields.Integer(string='Vehicle Sticker Issued Count')

    unit_condition = fields.Selection([
        ('pass', 'Passed - Pristine Condition'),
        ('minor_repairs', 'Conditional - Minor Repairs Required'),
        ('major_damage', 'Failed - Major Damage / Missing Items'),
    ], string='Condition Assessment', default='pass', tracking=True)
    
    chargeable_findings = fields.Text(string='Chargeable Findings & Damage List')
    tenant_signature = fields.Binary(string='Tenant Acknowledgment Signature')
    
    info_desk_verified = fields.Boolean(string='Information Desk Recording Verified')
    security_coordination = fields.Boolean(string='Security Coordination Cleared')
    wifi_parking_assigned = fields.Boolean(string='Parking / Access / Wi-Fi Assigned')
    
    unit_status_post_inspection = fields.Selection([
        ('occupied', 'Occupied'),
        ('vacated', 'Vacated'),
        ('under_repair', 'Under Repair'),
        ('under_cleaning', 'Under Cleaning'),
        ('available', 'Available'),
    ], string='Unit Status Post-Inspection', default='occupied')

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
            # Sync baseline meter readings and status back to Property Unit product
            if rec.unit_id:
                rec.unit_id.latest_electric_reading = rec.electric_reading
                rec.unit_id.latest_water_reading = rec.water_reading
                if rec.unit_status_post_inspection:
                    rec.unit_id.occupancy_status = rec.unit_status_post_inspection
