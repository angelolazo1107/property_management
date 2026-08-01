# -*- coding: utf-8 -*-
from odoo import models, fields

class ApprovalMatrix(models.Model):
    _name = 'approval.matrix'
    _description = 'Governance & Financial Approval Matrix'

    name = fields.Char(string='Matrix Rule Name', required=True)
    module = fields.Selection([
        ('Purchase', 'Purchase / Procurement'),
        ('Leasing', 'Leasing Operations'),
        ('PMO', 'PMO Operations'),
        ('Admin', 'Admin & Fleet Services'),
    ], string='Module / Scope', default='Purchase', required=True)
    transaction_type = fields.Char(string='Transaction Type', required=True)
    min_amount = fields.Monetary(string='Min Amount', currency_field='currency_id', default=0.0)
    max_amount = fields.Monetary(string='Max Amount', currency_field='currency_id', default=9999999.0)
    required_approvers = fields.Char(string='Required Approver Level(s)', required=True)
    escalation_approver = fields.Char(string='Escalation Approver')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    notes = fields.Text(string='Policy Notes / Description')
