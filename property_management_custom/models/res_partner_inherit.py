# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    is_tenant = fields.Boolean(string='Is Tenant', default=False)
    is_vendor = fields.Boolean(string='Is Vendor', default=False)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )

    tenant_unpaid_balance = fields.Monetary(
        string='Tenant Total Unpaid Balance', 
        currency_field='currency_id', 
        compute='_compute_tenant_unpaid_balance'
    )

    def _compute_tenant_unpaid_balance(self):
        for partner in self:
            invoices = self.env['account.move'].search([
                ('partner_id', '=', partner.id),
                ('move_type', '=', 'out_invoice'),
                ('payment_state', 'not in', ['paid', 'in_payment']),
                ('state', '=', 'posted')
            ])
            partner.tenant_unpaid_balance = sum(invoices.mapped('amount_residual'))
