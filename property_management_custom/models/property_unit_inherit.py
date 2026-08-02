# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

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

    @api.model
    def default_get(self, fields_list):
        res = super(ProductProductPropertyInherit, self).default_get(fields_list)
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        if php_currency:
            # Force PHP active and set symbol
            if not php_currency.active or php_currency.symbol != '₱':
                php_currency.sudo().write({'active': True, 'symbol': '₱', 'position': 'before'})
            # Force all companies in DB to PHP main currency
            companies = self.env['res.company'].search([])
            for comp in companies:
                if comp.currency_id != php_currency:
                    try:
                        comp.sudo().write({'currency_id': php_currency.id})
                    except Exception:
                        pass
        return res


class ProductTemplatePropertyInherit(models.Model):
    _inherit = 'product.template'

    @api.model
    def default_get(self, fields_list):
        res = super(ProductTemplatePropertyInherit, self).default_get(fields_list)
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        if php_currency:
            if not php_currency.active or php_currency.symbol != '₱':
                php_currency.sudo().write({'active': True, 'symbol': '₱', 'position': 'before'})
            companies = self.env['res.company'].search([])
            for comp in companies:
                if comp.currency_id != php_currency:
                    try:
                        comp.sudo().write({'currency_id': php_currency.id})
                    except Exception:
                        pass
        return res


class ResCompanyPropertyInherit(models.Model):
    _inherit = 'res.company'

    @api.model
    def default_get(self, fields_list):
        res = super(ResCompanyPropertyInherit, self).default_get(fields_list)
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        if php_currency:
            res['currency_id'] = php_currency.id
        return res

    def write(self, vals):
        if 'currency_id' in vals:
            for company in self:
                if vals['currency_id'] == company.currency_id.id:
                    vals_copy = dict(vals)
                    vals_copy.pop('currency_id', None)
                    return super(ResCompanyPropertyInherit, company).write(vals_copy)
        try:
            return super(ResCompanyPropertyInherit, self).write(vals)
        except UserError as e:
            if 'journal items already exist' in str(e).lower() or 'journal items' in str(e).lower():
                vals_copy = dict(vals)
                vals_copy.pop('currency_id', None)
                return super(ResCompanyPropertyInherit, self).write(vals_copy)
            raise e

