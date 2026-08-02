# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class LeaseContract(models.Model):
    _name = 'lease.contract'
    _description = 'Tenant Lease Contract Lifecycle & Legal Controls'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Lease Number', required=True, copy=False, readonly=True, default='New')
    tenant_id = fields.Many2one('res.partner', string='Tenant Name', required=True, tracking=True)
    unit_id = fields.Many2one(
        'product.product', 
        string='Assigned Property Unit', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    
    date_start = fields.Date(string='Lease Start Date', required=True, tracking=True)
    date_end = fields.Date(string='Lease End Date', required=True, tracking=True)
    contract_term_months = fields.Integer(string='Contract Term (Months)', default=12, tracking=True)
    payment_due_date = fields.Selection([
        ('1', 'Every 1st of the month'),
        ('5', 'Every 5th of the month'),
        ('10', 'Every 10th of the month'),
        ('15', 'Every 15th of the month'),
        ('30', 'Every 30th / End of month'),
    ], string='Payment Due Date', default='5', tracking=True)
    
    monthly_rent = fields.Monetary(string='Monthly Rental Amount', currency_field='currency_id', required=True, tracking=True)
    security_deposit = fields.Monetary(string='Security Deposit Amount', currency_field='currency_id', required=True, tracking=True)
    furniture_rental_fee = fields.Monetary(string='Furniture Rental Fee', currency_field='currency_id', tracking=True)
    parking_fee = fields.Monetary(string='Parking Fee', currency_field='currency_id', tracking=True)
    wifi_fee = fields.Monetary(string='Wi-Fi Fee', currency_field='currency_id', tracking=True)
    
    stage = fields.Selection([
        ('draft', 'Draft Contract'),
        ('tenant_review', 'For Tenant Review'),
        ('for_signing', 'For Signing'),
        ('signed_tenant', 'Signed by Tenant'),
        ('submitted_billing', 'Submitted to Billing'),
        ('submitted_legal', 'Submitted to Legal'),
        ('for_notarization', 'For Notarization'),
        ('notarized', 'Notarized'),
        ('released_tenant', 'Released to Tenant'),
        ('active', 'Active Lease'),
        ('move_out', 'Move-Out Inspection'),
        ('deposit_refund', 'Security Deposit Refunded'),
        ('terminated', 'Closed / Terminated'),
        ('archived', 'Archived'),
    ], string='Lease Contract Status', default='draft', tracking=True)

    renewal_terms = fields.Text(string='Renewal Terms & Escalation Clause')
    early_termination_clause = fields.Text(
        string='Early Termination Clause', 
        default="Early termination requires 60-day prior written notice. Remaining advance rent shall be applied, and security deposit forfeiture policy applies."
    )
    deposit_forfeiture_rule = fields.Text(
        string='Security Deposit Forfeiture Rule',
        default="Security deposit shall be forfeited in full in case of unnotified breach, pre-termination before 6-month lock-in, or unresolved property damage."
    )

    notary_status = fields.Selection([
        ('pending', 'Pending Notarization'),
        ('done', 'Notarized'),
    ], string='Notary Status', default='pending', tracking=True)

    signed_copy = fields.Binary(string='Signed Contract Copy')
    signed_copy_filename = fields.Char(string='Signed Copy File Name')

    bis_id = fields.Many2one('tenant.application.bis', string='Tenant BIS Reference')
    opportunity_id = fields.Many2one('crm.lead', string='Associated CRM Opportunity')

    bis_submitted = fields.Boolean(string='BIS Data Verified', tracking=True)
    legal_clearance = fields.Boolean(string='Legal Clearance Approved', tracking=True)
    deposit_paid = fields.Boolean(string='Security Deposit Paid (Accounting Verified)', tracking=True)
    move_in_checklist_done = fields.Boolean(string='PMO Move-In Checklist Completed', tracking=True)

    move_in_cleared = fields.Boolean(string='Move-In Clearance Granted', default=False, tracking=True)
    exception_approved = fields.Boolean(string='Management Exception Approved for Move-In', default=False, tracking=True)
    exception_reason = fields.Text(string='Management Exception Justification')
    
    # Move-Out & Deposit Settlement Ledger
    unpaid_rent_deduction = fields.Monetary(string='Unpaid Rent Deduction', currency_field='currency_id')
    utility_deduction = fields.Monetary(string='Utility Deduction', currency_field='currency_id')
    damage_deduction = fields.Monetary(string='Damage Charges Deduction', currency_field='currency_id')
    cleaning_deduction = fields.Monetary(string='Cleaning Charges Deduction', currency_field='currency_id')
    penalties_deduction = fields.Monetary(string='Penalties / Late Charges', currency_field='currency_id')
    missing_items_deduction = fields.Monetary(string='Missing Access Items Deduction', currency_field='currency_id')
    
    total_deductions = fields.Monetary(string='Total Deductions', currency_field='currency_id', compute='_compute_deductions', store=True)
    net_refund_amount = fields.Monetary(string='Net Security Deposit Refundable', currency_field='currency_id', compute='_compute_net_refund', store=True)
    
    deposit_refund_status = fields.Selection([
        ('pending', 'Pending Clearance'),
        ('approved', 'Refund Approved by GM'),
        ('processed', 'Accounting Voucher Prepared'),
        ('refunded', 'Deposit Refund Released'),
    ], string='Security Deposit Refund Status', default='pending', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id
    )
    notes = fields.Text(string='Contract Special Terms & Conditions')

    @api.depends('unpaid_rent_deduction', 'utility_deduction', 'damage_deduction', 'cleaning_deduction', 'penalties_deduction', 'missing_items_deduction')
    def _compute_deductions(self):
        for rec in self:
            rec.total_deductions = (
                (rec.unpaid_rent_deduction or 0.0) +
                (rec.utility_deduction or 0.0) +
                (rec.damage_deduction or 0.0) +
                (rec.cleaning_deduction or 0.0) +
                (rec.penalties_deduction or 0.0) +
                (rec.missing_items_deduction or 0.0)
            )

    @api.depends('security_deposit', 'total_deductions')
    def _compute_net_refund(self):
        for rec in self:
            rec.net_refund_amount = max(0.0, (rec.security_deposit or 0.0) - rec.total_deductions)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('lease.contract') or 'LEASE-2026-00001'
        return super(LeaseContract, self).create(vals)

    def action_submit_tenant_review(self):
        for rec in self:
            rec.stage = 'tenant_review'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> submitted for Tenant Review.", subject="For Tenant Review")

    def action_send_signing(self):
        for rec in self:
            rec.stage = 'for_signing'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> issued for Tenant Signature.", subject="For Signing")

    def action_tenant_signed(self):
        for rec in self:
            if not rec.signed_copy:
                raise UserError("Signed Copy Attachment Required: Please attach the executed contract copy before updating status to Signed by Tenant.")
            rec.stage = 'signed_tenant'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> signed by Tenant {rec.tenant_id.name}.", subject="Signed by Tenant")

    def action_submit_legal(self):
        for rec in self:
            rec.stage = 'submitted_legal'
            rec.legal_clearance = True
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> submitted to Legal for Notarization.", subject="Submitted to Legal")

    def action_notarize(self):
        for rec in self:
            rec.notary_status = 'done'
            rec.stage = 'notarized'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> successfully Notarized.", subject="Contract Notarized")

    def action_release_tenant(self):
        for rec in self:
            rec.stage = 'released_tenant'
            rec.message_post(body=f"Executed Lease Contract <b>{rec.name}</b> released to Tenant {rec.tenant_id.name}.", subject="Released to Tenant")

    def action_verify_move_in_clearance(self):
        """
        Important Control: No move-in should be allowed unless:
        1. BIS is approved.
        2. Required tenant documents are complete.
        3. Required payments are settled.
        4. Contract is signed or management-approved for exception.
        5. Unit assessment is complete.
        6. Move-In Form is prepared.
        """
        for rec in self:
            missing_criteria = []

            # 1. BIS Approved
            if not rec.bis_id or rec.bis_id.state != 'approved':
                missing_criteria.append("1. Approved Buyer/Tenant Information Sheet (BIS)")

            # 2. Required Tenant Documents Complete
            if rec.bis_id and (not rec.bis_id.valid_id or not rec.bis_id.proof_of_income):
                missing_criteria.append("2. Complete Tenant Documents (Valid ID & Proof of Income)")

            # 3. Required Payments Settled
            if not rec.deposit_paid:
                missing_criteria.append("3. Settled Security Deposit & Reservation Payment (Verified by Accounting)")

            # 4. Contract Signed or Management Exception Approved
            signed_stages = ['signed_tenant', 'submitted_legal', 'for_notarization', 'notarized', 'released_tenant', 'active']
            if rec.stage not in signed_stages and not rec.exception_approved:
                missing_criteria.append("4. Signed Lease Contract (or Management Exception Approval)")

            # 5. Unit Assessment & 6. Move-In Checklist
            if not rec.move_in_checklist_done:
                missing_criteria.append("5 & 6. Unit Assessment & Prepared PMO Move-In Turnover Form")

            if missing_criteria:
                error_msg = "MOVE-IN CLEARANCE BLOCKED:\nThe following required criteria must be fulfilled prior to move-in:\n\n"
                error_msg += "\n".join(missing_criteria)
                error_msg += "\n\nIf an urgent exception is authorized, check 'Management Exception Approved for Move-In'."
                raise UserError(error_msg)

            rec.move_in_cleared = True
            rec.stage = 'active'
            rec.unit_id.occupancy_status = 'occupied'
            rec.unit_id.current_tenant_id = rec.tenant_id

            if rec.opportunity_id:
                rec.opportunity_id.move_in_cleared = True

            rec.message_post(
                body=f"<b>MOVE-IN CLEARANCE GRANTED</b> for Tenant {rec.tenant_id.name} on Unit <b>{rec.unit_id.display_name}</b>. All 6 compliance criteria verified.",
                subject="Move-In Clearance Approved"
            )

    def action_trigger_move_out(self):
        for rec in self:
            rec.stage = 'move_out'
            rec.unit_id.occupancy_status = 'vacated'

    def action_approve_deposit_refund(self):
        for rec in self:
            rec.deposit_refund_status = 'approved'
            rec.stage = 'deposit_refund'

    def action_archive(self):
        for rec in self:
            rec.stage = 'archived'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> archived.", subject="Contract Archived")
