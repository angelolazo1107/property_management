# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_tenant = fields.Boolean(string='Is Tenant', default=False)
    is_vendor = fields.Boolean(string='Is Vendor', default=False)
