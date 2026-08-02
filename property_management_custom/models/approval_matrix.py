# -*- coding: utf-8 -*-
from odoo import models, fields

class ApprovalMatrix(models.Model):
    _name = 'approval.matrix'
    _description = 'Governance & Financial Approval Matrix'

    name = fields.Char(string='Matrix Rule Name', required=True)
    
    approval_category = fields.Selection([
        ('pr', '1. Purchase Requisition Approval'),
        ('canvass', '2. Strategic Sourcing / Canvass Approval'),
        ('po', '3. Purchase Order Approval'),
        ('payment_request', '4. Payment Request Approval'),
        ('osr', '5. Office Supplies Request Approval'),
        ('vehicle_errand', '6. Vehicle Errand Request Approval'),
        ('special_client_trip', '7. Special Client Trip Approval'),
        ('pmo_job_order', '8. PMO Job Order Approval'),
        ('deposit_refund', '9. Security Deposit Refund Approval'),
        ('deposit_deduction', '10. Security Deposit Deduction Approval'),
        ('lease_discount', '11. Lease Discount Approval'),
        ('mgmt_exception', '12. Management Exception Approval'),
        ('move_in_exception', '13. Move-In Exception Approval'),
        ('move_out_exception', '14. Move-Out Exception Approval'),
        ('jo_waiver', '15. Job Order Waiver Approval'),
        ('vehicle_waiver', '16. Vehicle Charge Waiver Approval'),
    ], string='Approval Category', default='pr', required=True)

    module = fields.Selection([
        ('Purchase', 'Purchase / Procurement'),
        ('Leasing', 'Leasing Operations'),
        ('PMO', 'PMO Operations'),
        ('Admin', 'Admin & Fleet Services'),
        ('Accounting', 'Accounting & Finance'),
    ], string='Module / Scope', default='Purchase', required=True)

    transaction_type = fields.Char(string='Transaction Scope / Condition', required=True)
    min_amount = fields.Monetary(string='Min Amount Threshold', currency_field='currency_id', default=0.0)
    max_amount = fields.Monetary(string='Max Amount Threshold', currency_field='currency_id', default=9999999.0)
    required_approvers = fields.Char(string='Required Approver Role(s)', required=True)
    escalation_approver = fields.Char(string='Escalation Approver (GM / Board)')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    notes = fields.Text(string='Policy Notes & Governance Guidelines')
