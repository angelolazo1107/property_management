# -*- coding: utf-8 -*-
from odoo import models, fields, api

class OfficeSupplyRequest(models.Model):
    _name = 'office.supply.request'
    _description = 'Monthly Office Supply Requisition'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Requisition Ref', required=True, copy=False, readonly=True, default='New')
    department_id = fields.Many2one('hr.department', string='Requesting Department')
    requested_by_id = fields.Many2one('res.users', string='Requestor Name', default=lambda self: self.env.user, required=True)
    request_date = fields.Date(string='Request Date', default=fields.Date.context_today, required=True)

    line_ids = fields.One2many('office.supply.request.line', 'request_id', string='Supplies Items List')

    status = fields.Selection([
        ('draft', 'Draft Requisition'),
        ('dept_approved', 'Dept Head Approved'),
        ('admin_review', 'Admin Stock Verified'),
        ('released', 'Inventory Released'),
        ('pr_raised', 'Sent to Procurement'),
    ], string='Status', default='draft', tracking=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('office.supply.request') or 'SUPPLY-0001'
        return super(OfficeSupplyRequest, self).create(vals)

    def action_dept_approve(self):
        for rec in self:
            rec.status = 'dept_approved'


class OfficeSupplyRequestLine(models.Model):
    _name = 'office.supply.request.line'
    _description = 'Office Supply Requisition Item'

    request_id = fields.Many2one('office.supply.request', string='Requisition Reference', ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Supply Item / Product', required=True)
    quantity = fields.Float(string='Requested Quantity', default=1.0, required=True)
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')
    notes = fields.Char(string='Remarks / Purpose')
