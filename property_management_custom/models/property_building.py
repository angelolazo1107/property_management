# -*- coding: utf-8 -*-
from odoo import models, fields

class PropertyBuilding(models.Model):
    _name = 'x_buildings'
    _description = 'Property Buildings'

    name = fields.Char(string='Building Name')
