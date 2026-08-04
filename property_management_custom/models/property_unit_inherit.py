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

    property_type = fields.Selection([
        ('commercial', 'Commercial Retail'),
        ('office', 'Office Suite'),
        ('residential_studio', 'Residential Studio'),
        ('residential_1br', 'Residential 1-Bedroom'),
        ('residential_2br', 'Residential 2-Bedroom'),
        ('residential_penthouse', 'Executive Penthouse'),
        ('warehouse', 'Industrial Warehouse'),
    ], string='Property Type', default='residential_studio', tracking=True)

    property_address = fields.Char(string='Property Full Address', tracking=True)

    current_tenant_id = fields.Many2one('res.partner', string='Current Tenant', tracking=True)
    electricity_meter_no = fields.Char(string='Electricity Meter ID')
    water_meter_no = fields.Char(string='Water Meter ID')
    latest_electric_reading = fields.Float(string='Latest Electric Reading (kWh)')
    latest_water_reading = fields.Float(string='Latest Water Reading (cbm)')


class ResCompanyCurrencyFix(models.Model):
    _inherit = 'res.company'

    def write(self, vals):
        if 'currency_id' in vals:
            currency_id = vals['currency_id']
            for company in self:
                if currency_id and company.currency_id.id != currency_id:
                    self.env.cr.execute(
                        "UPDATE res_company SET currency_id = %s WHERE id = %s",
                        (currency_id, company.id)
                    )
                    company.invalidate_recordset(['currency_id'])
            vals_copy = dict(vals)
            vals_copy.pop('currency_id', None)
            return super(ResCompanyCurrencyFix, self).write(vals_copy)
        return super(ResCompanyCurrencyFix, self).write(vals)
