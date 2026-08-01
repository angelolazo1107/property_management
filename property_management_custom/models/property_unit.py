# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = 'Property Building / Tower'

    name = fields.Char(string='Building / Tower Name', required=True)
    code = fields.Char(string='Building Code')
    address = fields.Char(string='Physical Address')
    total_floors = fields.Integer(string='Total Floors')
    total_units = fields.Integer(string='Total Units Count')
    notes = fields.Text(string='Description / Amenities')


class PropertyUnit(models.Model):
    _name = 'property.unit'
    _description = 'Property Unit'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Unit Number / Code', required=True, tracking=True)
    building_id = fields.Many2one('property.building', string='Building / Tower', required=True)
    floor = fields.Char(string='Floor Level', required=True)
    
    unit_type = fields.Selection([
        ('commercial', 'Commercial Space'),
        ('residential', 'Residential Suite'),
        ('office', 'Office Space'),
        ('parking', 'Parking Slot'),
        ('warehouse', 'Warehouse Storage'),
    ], string='Unit Category', default='residential', required=True, tracking=True)
    
    area_sqm = fields.Float(string='Floor Area (sqm)', digits=(16, 2), required=True)
    monthly_rate = fields.Monetary(string='Base Monthly Rent', currency_field='currency_id', required=True, tracking=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Under Maintenance'),
        ('blocked', 'Blocked / Out of Service'),
    ], string='Occupancy Status', default='available', tracking=True)

    current_tenant_id = fields.Many2one('res.partner', string='Current Tenant', tracking=True)
    electricity_meter_no = fields.Char(string='Electricity Meter ID')
    water_meter_no = fields.Char(string='Water Meter ID')
    latest_electric_reading = fields.Float(string='Latest Electric Reading (kWh)')
    latest_water_reading = fields.Float(string='Latest Water Reading (cbm)')
    
    notes = fields.Text(string='Unit Features & Remarks')
