# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    pr_reference = fields.Char(string='Purchase Request (PR) Ref')
    pr_justification = fields.Text(string='PR Justification / Reason')
    
    # 3-Supplier Canvass & Strategic Sourcing Fields
    canvass_attachment = fields.Binary(string='Supplier Comparison / Canvass Sheet')
    canvass_file_name = fields.Char(string='Canvass File Name')
    supplier_1_name = fields.Char(string='Supplier 1 Name & Price Quote')
    supplier_2_name = fields.Char(string='Supplier 2 Name & Price Quote')
    supplier_3_name = fields.Char(string='Supplier 3 Name & Price Quote')
    
    # Repeat Order Sourcing Controls
    is_repeat_order = fields.Boolean(string='Is Repeat Order', default=False)
    previous_po_id = fields.Many2one('purchase.order', string='Previous PO Reference (within 6 Months)')
    price_increased = fields.Boolean(string='Price Increased vs Previous PO', default=False)

    # Approvals Engine Integration
    dept_head_approved = fields.Boolean(string='Dept Head Approved PR', readonly=True, copy=False)
    dept_head_approver_id = fields.Many2one('res.users', string='Dept Head Approver', readonly=True)
    
    procurement_manager_approved = fields.Boolean(string='Procurement Manager Approved Canvass', readonly=True, copy=False)
    gm_approved = fields.Boolean(string='General Manager Approved PR & Sourcing', readonly=True, copy=False)
    gm_po_approved = fields.Boolean(string='GM Purchase Order Approved (Required for PO Email)', readonly=True, copy=False)
    gm_approver_id = fields.Many2one('res.users', string='GM Approver', readonly=True)

    # 3-Way Match Checkpoint
    goods_receipt_matched = fields.Boolean(string='Goods Receipt (GR) Matched', copy=False)
    invoice_matched = fields.Boolean(string='Vendor Invoice Matched', copy=False)
    three_way_match_verified = fields.Boolean(string='3-Way Match Verified (PO + GR + Invoice)', copy=False)
    payment_request_cleared = fields.Boolean(string='Accounting Payment Request Cleared', copy=False)

    def action_dept_head_approve(self):
        for rec in self:
            rec.dept_head_approved = True
            rec.dept_head_approver_id = self.env.user

    def action_procurement_manager_approve(self):
        for rec in self:
            rec.procurement_manager_approved = True

    def action_gm_approve(self):
        for rec in self:
            rec.gm_approved = True
            rec.gm_po_approved = True
            rec.gm_approver_id = self.env.user

    def action_verify_three_way_match(self):
        for rec in self:
            if not (rec.goods_receipt_matched and rec.invoice_matched):
                raise UserError("3-Way Match Incomplete: Both Goods Receipt and Vendor Invoice must be verified against PO!")
            rec.three_way_match_verified = True
            rec.payment_request_cleared = True

    def button_confirm(self):
        for rec in self:
            if not rec.dept_head_approved:
                raise UserError("Procurement Governance: Department Head approval is required before confirming Purchase Order.")
            if not rec.gm_po_approved:
                raise UserError("Procurement Governance: General Manager PO approval is required before issuing Purchase Order.")
        return super(PurchaseOrderInherit, self).button_confirm()
