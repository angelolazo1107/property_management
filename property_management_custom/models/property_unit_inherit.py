# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductProductPropertyInherit(models.Model):
    _inherit = 'product.product'

    is_property_unit = fields.Boolean(string='Is Property Unit / Commercial Space', default=False)
    floor_level = fields.Char(string='Floor Level')
    area_sqm = fields.Float(string='Floor Area (sqm)', digits=(16, 2))
    
    occupancy_status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('vacated', 'Vacated / Turnover'),
        ('under_repair', 'Under Repair'),
        ('under_cleaning', 'Under Cleaning'),
        ('maintenance', 'Under Maintenance'),
        ('blocked', 'Blocked / Out of Service'),
    ], string='Occupancy Status', default='available', tracking=True)

    current_tenant_id = fields.Many2one('res.partner', string='Current Tenant', tracking=True)
    electricity_meter_no = fields.Char(string='Electricity Meter ID')
    water_meter_no = fields.Char(string='Water Meter ID')
    latest_electric_reading = fields.Float(string='Latest Electric Reading (kWh)')
    latest_water_reading = fields.Float(string='Latest Water Reading (cbm)')
