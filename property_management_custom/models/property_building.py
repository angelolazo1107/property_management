# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = 'Property Building / Real Estate Complex'
    _order = 'name asc'

    name = fields.Char(string='Building / Tower Name', required=True, tracking=True)
    code = fields.Char(string='Building Code', copy=False)
    address = fields.Text(string='Building Address')
    total_floors = fields.Integer(string='Total Floor Levels', default=1)
    
    unit_ids = fields.One2many('product.product', 'building_id', string='Property Units')
    unit_count = fields.Integer(string='Total Units Count', compute='_compute_unit_count')

    active = fields.Boolean(string='Active', default=True)

    @api.depends('unit_ids')
    def _compute_unit_count(self):
        for rec in self:
            rec.unit_count = len(rec.unit_ids)
