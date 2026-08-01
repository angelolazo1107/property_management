# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    pr_reference = fields.Char(string='Purchase Request (PR) Ref')
    canvass_attachment = fields.Binary(string='Supplier Comparison / Canvass Sheet')
    canvass_file_name = fields.Char(string='Canvass File Name')

    dept_head_approved = fields.Boolean(string='Dept Head Approved', readonly=True, copy=False)
    dept_head_approver_id = fields.Many2one('res.users', string='Dept Head Approver', readonly=True)
    
    gm_approved = fields.Boolean(string='General Manager Approved', readonly=True, copy=False)
    gm_approver_id = fields.Many2one('res.users', string='GM Approver', readonly=True)

    def action_dept_head_approve(self):
        for rec in self:
            rec.dept_head_approved = True
            rec.dept_head_approver_id = self.env.user

    def action_gm_approve(self):
        for rec in self:
            rec.gm_approved = True
            rec.gm_approver_id = self.env.user

    def button_confirm(self):
        for rec in self:
            if not rec.dept_head_approved:
                raise UserError("Procurement Governance: Department Head approval is required before confirming Purchase Order.")
            if rec.amount_total > 50000.0 and not rec.gm_approved:
                raise UserError("Procurement Governance: General Manager approval is required for POs exceeding ₱50,000.")
        return super(PurchaseOrderInherit, self).button_confirm()
