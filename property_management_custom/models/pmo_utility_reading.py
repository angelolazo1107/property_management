# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PMOUtilityReading(models.Model):
    _name = 'pmo.utility.reading'
    _description = 'Monthly PMO Utility Meter Readings'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reading Ref', required=True, copy=False, readonly=True, default='New')
    unit_id = fields.Many2one('product.product', string='Property Unit', domain="[('is_property_unit', '=', True)]", required=True, tracking=True)
    tenant_id = fields.Many2one('res.partner', string='Tenant Name')
    reading_date = fields.Date(string='Reading Date', default=fields.Date.context_today, required=True)
    
    meter_type = fields.Selection([
        ('electricity', 'Electricity Meter (kWh)'),
        ('water', 'Water Meter (cbm)'),
    ], string='Utility Meter Type', default='electricity', required=True)

    previous_reading = fields.Float(string='Previous Meter Reading', required=True)
    current_reading = fields.Float(string='Current Meter Reading', required=True)
    consumption = fields.Float(string='Consumption Units', compute='_compute_consumption', store=True)
    
    rate_per_unit = fields.Monetary(string='Rate per Unit', currency_field='currency_id', required=True)
    total_amount = fields.Monetary(string='Total Billable Amount', currency_field='currency_id', compute='_compute_total', store=True)
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    status = fields.Selection([
        ('draft', 'Draft'),
        ('verified', 'Verified by Admin'),
        ('billed', 'Invoiced to Tenant'),
    ], string='Status', default='draft', tracking=True)

    @api.depends('previous_reading', 'current_reading')
    def _compute_consumption(self):
        for rec in self:
            rec.consumption = max(0.0, rec.current_reading - rec.previous_reading)

    @api.depends('consumption', 'rate_per_unit')
    def _compute_total(self):
        for rec in self:
            rec.total_amount = rec.consumption * rec.rate_per_unit

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('pmo.utility.reading') or 'UTIL-0001'
        return super(PMOUtilityReading, self).create(vals_list)

    def action_verify_reading(self):
        for rec in self:
            rec.status = 'verified'
            if rec.unit_id:
                if rec.meter_type == 'electricity':
                    rec.unit_id.latest_electric_reading = rec.current_reading
                elif rec.meter_type == 'water':
                    rec.unit_id.latest_water_reading = rec.current_reading
