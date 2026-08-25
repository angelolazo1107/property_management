# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _inherit = 'property.building'

    code = fields.Char(string='Building Code', copy=False)
    total_floors = fields.Integer(string='Total Floor Levels', default=1)
