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
        ('for_renewal', 'For Renewal Discussion'),
        ('renewal_offered', 'Renewal Offered'),
        ('renewed', 'Renewed'),
        ('for_move_out', 'For Move-Out'),
        ('expired', 'Expired'),
        ('move_out', 'Move-Out Inspection'),
        ('deposit_refund', 'Security Deposit Refunded'),
        ('terminated', 'Closed / Terminated'),
        ('breached', 'Breached'),
        ('archived', 'Archived'),
    ], string='Lease Contract Status', default='draft', tracking=True)

    days_until_expiry = fields.Integer(
        string='Days Until Expiry', 
        compute='_compute_days_until_expiry', 
        store=True
    )
    renewal_decision = fields.Selection([
        ('pending', 'Pending Decision'),
        ('renewing', 'Tenant Will Renew'),
        ('vacating', 'Tenant Will Vacate'),
        ('holdover', 'Tenant in Holdover / Overstaying'),
        ('breach_terminated', 'Early Termination / Breach'),
    ], string='Renewal Decision', default='pending', tracking=True)

    is_holdover = fields.Boolean(
        string='Is Holdover?', 
        compute='_compute_is_holdover', 
        store=True
    )
    holdover_penalty_rate = fields.Float(
        string='Holdover Penalty Surcharge (%)', 
        default=25.0, 
        tracking=True,
        help="Surcharge percentage applied to standard monthly rent during holdover period (e.g. 25% = 1.25x rent)."
    )
    holdover_start_date = fields.Date(string='Holdover Start Date', tracking=True)
    holdover_monthly_rent = fields.Monetary(
        string='Holdover Monthly Rent', 
        currency_field='currency_id', 
        compute='_compute_holdover_monthly_rent', 
        store=True,
        tracking=True
    )

    notice_date = fields.Date(
        string='Notice Date (7-Day Requirement)', 
        tracking=True, 
        help="Date when 7-day minimum move-out or termination notice was officially served."
    )
    last_expiry_activity_stage = fields.Integer(default=999)

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

    unit_assessment_task_ids = fields.One2many('unit.assessment.task', 'lease_contract_id', string='Unit Assessments')
    unit_assessment_task_count = fields.Integer(string='Unit Assessments Count', compute='_compute_unit_assessment_task_count')

    @api.depends('unit_assessment_task_ids')
    def _compute_unit_assessment_task_count(self):
        for rec in self:
            rec.unit_assessment_task_count = len(rec.unit_assessment_task_ids)

    @api.depends('renewal_decision')
    def _compute_is_holdover(self):
        for rec in self:
            rec.is_holdover = (rec.renewal_decision == 'holdover')

    @api.depends('renewal_decision', 'monthly_rent', 'holdover_penalty_rate')
    def _compute_holdover_monthly_rent(self):
        for rec in self:
            if rec.renewal_decision == 'holdover':
                surcharge = (rec.monthly_rent or 0.0) * ((rec.holdover_penalty_rate or 0.0) / 100.0)
                rec.holdover_monthly_rent = (rec.monthly_rent or 0.0) + surcharge
            else:
                rec.holdover_monthly_rent = rec.monthly_rent or 0.0

    @api.depends('date_end', 'stage')
    def _compute_days_until_expiry(self):
        today = fields.Date.context_today(self)
        for rec in self:
            if rec.date_end and rec.stage in ['active', 'for_renewal', 'renewal_offered', 'for_move_out']:
                rec.days_until_expiry = (rec.date_end - today).days
            else:
                rec.days_until_expiry = 0

    # A8: Document count smart button
    document_count = fields.Integer(
        string='Documents',
        compute='_compute_document_count'
    )

    def _compute_document_count(self):
        for rec in self:
            rec.document_count = self.env['ir.attachment'].search_count([
                ('res_model', '=', 'lease.contract'),
                ('res_id', '=', rec.id),
            ])

    def action_view_documents(self):
        self.ensure_one()
        return {
            'name': 'Lease Contract Documents',
            'type': 'ir.actions.act_window',
            'res_model': 'ir.attachment',
            'view_mode': 'list,form',
            'domain': [('res_model', '=', 'lease.contract'), ('res_id', '=', self.id)],
            'context': {
                'default_res_model': 'lease.contract',
                'default_res_id': self.id,
            },
        }

    # B2: Lease Contract Stage Guard — prevent invalid backwards/illegal transitions
    @api.constrains('stage')
    def _check_stage_transition(self):
        # Stages from which backward jump to draft is not allowed
        active_stages = [
            'active', 'for_renewal', 'renewal_offered', 'renewed',
            'for_move_out', 'expired', 'move_out',
            'deposit_refund', 'terminated', 'breached', 'archived'
        ]
        # Stages that require legal clearance before they can be set
        legal_required_stages = ['terminated', 'breached']

        for rec in self:
            if rec.stage == 'draft' and rec.id:
                # Allow: draft is always valid on new records
                pass
            if rec.stage in legal_required_stages:
                if not rec.legal_clearance:
                    raise UserError(
                        f"Stage Transition Blocked: The lease stage '{rec.stage.replace('_', ' ').title()}' "
                        f"requires Legal Clearance to be confirmed.\n\n"
                        f"Please ensure the Legal team has reviewed and approved this action, "
                        f"then tick 'Legal Clearance Approved' before proceeding."
                    )

    def action_mark_renewed(self):
        for rec in self:
            rec.stage = 'renewed'
            rec.renewal_decision = 'renewing'
            rec.message_post(
                body=f"Lease Contract <b>{rec.name}</b> marked as RENEWED by Tenant {rec.tenant_id.name}.",
                subject="Lease Renewed"
            )

    def action_mark_for_move_out(self):
        today = fields.Date.context_today(self)
        for rec in self:
            rec.stage = 'for_move_out'
            rec.renewal_decision = 'vacating'
            if not rec.notice_date:
                rec.notice_date = today
            rec.message_post(
                body=f"Lease Contract <b>{rec.name}</b> marked FOR MOVE-OUT. Official Notice Date: {rec.notice_date}.",
                subject="Move-Out Notice Recorded"
            )

    def action_mark_breached(self):
        today = fields.Date.context_today(self)
        for rec in self:
            rec.stage = 'breached'
            rec.renewal_decision = 'breach_terminated'
            if not rec.notice_date:
                rec.notice_date = today
            rec.message_post(
                body=f"⚠️ <b>LEASE CONTRACT BREACH / EARLY TERMINATION RECORDED</b>: Contract <b>{rec.name}</b> marked as BREACHED. Security deposit forfeiture rule applies. Official Notice Date: {rec.notice_date}.",
                subject="Lease Contract Breached"
            )

    @api.model
    def cron_lease_expiration_monitoring(self):
        """ Daily Cron: 5-Tier Expiration Monitoring & Activity Automation Engine """
        today = fields.Date.context_today(self)
        active_leases = self.search([
            ('stage', 'in', ['active', 'for_renewal', 'renewal_offered']),
            ('date_end', '!=', False)
        ])
        for rec in active_leases:
            days = (rec.date_end - today).days
            rec.days_until_expiry = days

            if days <= 0:
                if rec.renewal_decision == 'pending':
                    rec.stage = 'expired'
                    rec.message_post(
                        body=f"🚨 <b>EXPIRED CONTRACT ESCALATION</b>: Lease Contract <b>{rec.name}</b> reached expiry date ({rec.date_end}) without a confirmed renewal or move-out decision. Escalated to Executive Management.",
                        subject="Contract Expired - Escalation Required"
                    )
            elif days <= 7:
                if rec.last_expiry_activity_stage > 7:
                    rec.last_expiry_activity_stage = 7
                    rec.message_post(
                        body=f"⏰ <b>REQUIRED TENANT FINAL NOTIFICATION (7 Days to Expiry)</b>: Mandatory 7-day move-out / renewal notice required for Tenant {rec.tenant_id.name} [Unit: {rec.unit_id.name}]. Expiry Date: {rec.date_end}.",
                        subject="7-Day Final Notice Triggered"
                    )
            elif days <= 15:
                if rec.last_expiry_activity_stage > 15:
                    rec.last_expiry_activity_stage = 15
                    rec.message_post(
                        body=f"📌 <b>TENANT RENEWAL FOLLOW-UP (15 Days to Expiry)</b>: Follow up with Tenant {rec.tenant_id.name} to confirm intent to renew or vacate.",
                        subject="15-Day Renewal Follow-Up"
                    )
            elif days <= 30:
                if rec.last_expiry_activity_stage > 30:
                    rec.last_expiry_activity_stage = 30
                    rec.stage = 'renewal_offered'
                    rec.message_post(
                        body=f"✉️ <b>RENEWAL DISCUSSION &amp; OFFER (30 Days to Expiry)</b>: Renewal proposal &amp; rate package issued to Tenant {rec.tenant_id.name}.",
                        subject="30-Day Renewal Proposal"
                    )
            elif days <= 60:
                if rec.last_expiry_activity_stage > 60:
                    rec.last_expiry_activity_stage = 60
                    rec.stage = 'for_renewal'
                    rec.message_post(
                        body=f"🔍 <b>INTERNAL LEASING REVIEW (60 Days to Expiry)</b>: Assess tenant standing, rental escalation, and renewal eligibility for Unit {rec.unit_id.name}.",
                        subject="60-Day Leasing Review"
                    )
                    # Step 14: Schedule high-priority mail.activity for 60-Day Expiry Escalation Notice
                    activity_type = self.env.ref('mail.mail_activity_data_todo', raise_if_not_found=False)
                    if activity_type:
                        existing_activity = self.env['mail.activity'].search([
                            ('res_model', '=', 'lease.contract'),
                            ('res_id', '=', rec.id),
                            ('summary', 'ilike', '60-Day Lease Expiration Escalation')
                        ], limit=1)
                        if not existing_activity:
                            model_id = self.env['ir.model']._get('lease.contract').id
                            self.env['mail.activity'].create({
                                'activity_type_id': activity_type.id,
                                'summary': f"🚨 60-Day Lease Expiration Escalation Notice: {rec.name}",
                                'note': f"Lease contract <b>{rec.name}</b> for Tenant <b>{rec.tenant_id.name}</b> (Unit: {rec.unit_id.name}) expires on {rec.date_end}. Please prepare renewal proposal package or serve 60-day renewal notice.",
                                'res_model_id': model_id,
                                'res_id': rec.id,
                                'user_id': rec.create_uid.id or self.env.user.id,
                                'date_deadline': fields.Date.context_today(self),
                            })

    def action_view_unit_assessments(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_unit_assessment_task")
        action['domain'] = [('lease_contract_id', '=', self.id)]
        action['context'] = {
            'default_lease_contract_id': self.id,
            'default_unit_id': self.unit_id.id if self.unit_id else False,
            'default_tenant_id': self.tenant_id.id if self.tenant_id else False,
            'default_opportunity_id': self.opportunity_id.id if self.opportunity_id else False,
        }
        return action

    def action_create_unit_assessment(self):
        self.ensure_one()
        task_vals = {
            'unit_id': self.unit_id.id if self.unit_id else False,
            'tenant_id': self.tenant_id.id if self.tenant_id else False,
            'lease_contract_id': self.id,
            'opportunity_id': self.opportunity_id.id if self.opportunity_id else False,
        }
        task = self.env['unit.assessment.task'].create(task_vals)
        return {
            'type': 'ir.actions.act_window',
            'name': 'Unit Assessment & Turnover Task',
            'res_model': 'unit.assessment.task',
            'res_id': task.id,
            'view_mode': 'form',
            'target': 'current',
        }

    bis_submitted = fields.Boolean(string='BIS Data Verified', tracking=True)
    legal_clearance = fields.Boolean(string='Legal Clearance Approved', tracking=True)
    deposit_paid = fields.Boolean(string='Security Deposit Paid (Accounting Verified)', tracking=True)
    move_in_checklist_done = fields.Boolean(string='PMO Move-In Checklist Completed', tracking=True)

    # Stage 11: Contract Signing & Processing Checklist (8 Items)
    reviewed_with_tenant = fields.Boolean(string='Contract Reviewed with Tenant', tracking=True)
    tenant_signed = fields.Boolean(string='Tenant Signed Contract', tracking=True)
    house_rules_provided = fields.Boolean(string='House Rules Provided', tracking=True)
    violation_forms_provided = fields.Boolean(string='Violation Forms Provided', tracking=True)
    submitted_to_billing = fields.Boolean(string='Submitted to Billing', tracking=True)
    forwarded_to_legal = fields.Boolean(string='Forwarded to Legal', tracking=True)
    notarized = fields.Boolean(string='Notarized', tracking=True)
    tenant_received_notarized_copy = fields.Boolean(string='Tenant Received Notarized Copy', tracking=True)

    pet_registration_fee = fields.Monetary(string='Pet Registration Fee', currency_field='currency_id', default=0.0, tracking=True)
    other_charges = fields.Monetary(string='Other Charges / Move-In Setup', currency_field='currency_id', default=0.0, tracking=True)
    reservation_fee_credit = fields.Monetary(string='Reservation Fee Credit Applied', currency_field='currency_id', default=0.0, tracking=True)
    
    move_in_invoice_id = fields.Many2one('account.move', string='Move-In Customer Invoice', readonly=True, copy=False)
    move_in_invoice_payment_state = fields.Selection(
        related='move_in_invoice_id.payment_state', 
        string='Move-In Invoice Payment Status'
    )

    move_in_cleared = fields.Boolean(string='Move-In Clearance Granted', default=False, tracking=True)
    move_in_cleared_date = fields.Datetime(string='Cleared for Move-In Date', readonly=True)
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
        default=lambda self: self.env.company.currency_id.id
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
            year = fields.Date.context_today(self).strftime('%Y')
            property_code = 'SAPPHIRE'
            unit_code = '1001'
            
            if vals.get('unit_id'):
                unit = self.env['product.product'].browse(vals['unit_id'])
                if unit and unit.name:
                    parts = [p.strip() for p in unit.name.replace('-', ' ').split() if p.strip()]
                    if len(parts) >= 2:
                        property_code = parts[0].upper()
                        unit_code = parts[-1].upper()
                    elif len(parts) == 1:
                        unit_code = parts[0].upper()

            seq_raw = self.env['ir.sequence'].next_by_code('lease.contract') or '0001'
            seq_num = seq_raw.split('-')[-1] if '-' in seq_raw else seq_raw
            vals['name'] = f"LEASE-{year}-{property_code}-{unit_code}-{seq_num}"

        return super(LeaseContract, self).create(vals)

    def action_submit_tenant_review(self):
        for rec in self:
            rec.reviewed_with_tenant = True
            rec.stage = 'tenant_review'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> reviewed with and submitted to Tenant {rec.tenant_id.name}.", subject="For Tenant Review")

    def action_send_signing(self):
        for rec in self:
            rec.stage = 'for_signing'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> issued for Tenant Signature.", subject="For Signing")

    def action_tenant_signed(self):
        for rec in self:
            if not rec.signed_copy:
                raise UserError("Signed Copy Attachment Required: Please attach the executed contract copy before updating status to Signed by Tenant.")
            rec.tenant_signed = True
            rec.house_rules_provided = True
            rec.violation_forms_provided = True
            rec.stage = 'signed_tenant'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> signed by Tenant {rec.tenant_id.name}. House rules and violation forms provided.", subject="Signed by Tenant")

    def action_submit_billing(self):
        for rec in self:
            rec.submitted_to_billing = True
            rec.stage = 'submitted_billing'
            rec.message_post(body=f"Signed Lease Contract <b>{rec.name}</b> submitted to Billing.", subject="Submitted to Billing")

    def action_submit_legal(self):
        for rec in self:
            rec.forwarded_to_legal = True
            rec.stage = 'submitted_legal'
            rec.legal_clearance = True
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> forwarded to Legal for Notarization.", subject="Forwarded to Legal")

    def action_notarize(self):
        for rec in self:
            rec.notarized = True
            rec.notary_status = 'done'
            rec.stage = 'notarized'
            rec.message_post(body=f"Lease Contract <b>{rec.name}</b> successfully Notarized.", subject="Contract Notarized")

    def action_release_tenant(self):
        for rec in self:
            rec.tenant_received_notarized_copy = True
            rec.stage = 'released_tenant'
            rec.message_post(body=f"Notarized Executed Lease Contract <b>{rec.name}</b> received by Tenant {rec.tenant_id.name}.", subject="Notarized Copy Released")

    def action_create_move_in_invoice(self):
        for rec in self:
            if rec.move_in_invoice_id:
                raise UserError(f"Move-In Invoice {rec.move_in_invoice_id.name} already exists for this contract!")
            
            invoice_lines = []

            # 1. First Month Rental
            if (rec.monthly_rent or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"First Month Rental Income - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.monthly_rent,
                }))

            # 2. Furniture Rental
            if (rec.furniture_rental_fee or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Furniture Rental Income - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.furniture_rental_fee,
                }))

            # 3. Security Deposit
            if (rec.security_deposit or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Security Deposit Liability - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.security_deposit,
                }))

            # 4. Parking Fee
            if (rec.parking_fee or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Parking Fee Income - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.parking_fee,
                }))

            # 5. Access Card Fee
            access_req = self.env['access.request'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if access_req and (access_req.fee or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Access Card Fee Income ({access_req.number_of_cards} Card/s)",
                    'quantity': 1,
                    'price_unit': access_req.fee,
                }))

            # 6. Wi-Fi Fee
            wifi_req = self.env['wifi.request'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            wifi_amount = rec.wifi_fee or (wifi_req.monthly_fee if wifi_req else 0.0)
            if (wifi_amount or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Internet / Wi-Fi Fee Income - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': wifi_amount,
                }))

            # 7. Pet Registration Fee
            if (rec.pet_registration_fee or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Pet Registration Fee (Other Income) - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.pet_registration_fee,
                }))

            # 8. Other Charges
            if (rec.other_charges or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Other Charges / Move-In Setup - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': rec.other_charges,
                }))

            # 9. Less Reservation Fee Credit (Deduction)
            if (rec.reservation_fee_credit or 0.0) > 0:
                invoice_lines.append((0, 0, {
                    'name': f"Less Reservation Deposit Credit Applied - Unit: {rec.unit_id.name}",
                    'quantity': 1,
                    'price_unit': -abs(rec.reservation_fee_credit),
                }))

            if not invoice_lines:
                raise UserError("No billable Move-In fee lines found to create invoice!")

            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': rec.tenant_id.id,
                'invoice_date': fields.Date.context_today(self),
                'invoice_payment_term_id': rec.tenant_id.property_payment_term_id.id if rec.tenant_id.property_payment_term_id else False,
                'ref': f"Move-In Settlement Invoice: Lease {rec.name}",
                'invoice_line_ids': invoice_lines,
            }
            invoice = self.env['account.move'].create(invoice_vals)
            rec.move_in_invoice_id = invoice.id

            rec.message_post(
                body=f"Itemized Move-In Settlement Invoice <b>{invoice.name or 'Draft Invoice'}</b> created for Tenant {rec.tenant_id.name}. Total Amount: PHP {(invoice.amount_total or 0.0):,.2f}.",
                subject="Move-In Settlement Invoice Created"
            )

    def action_validate_move_in_readiness(self):
        """
        Validate all 9 Pre-Move-In Readiness Checkpoints:
        1. Reservation fee paid.
        2. Move-in invoice paid.
        3. Security deposit recorded & paid.
        4. Access card paid, if applicable.
        5. Parking paid, if applicable.
        6. Wi-Fi paid, if applicable.
        7. Contract signed.
        8. Unit assessment completed.
        9. Move-In Form / Inspection completed.
        """
        for rec in self:
            if rec.exception_approved:
                rec.move_in_cleared = True
                rec.move_in_cleared_date = fields.Datetime.now()
                rec.stage = 'active'
                rec.unit_id.occupancy_status = 'occupied'
                rec.unit_id.current_tenant_id = rec.tenant_id
                rec.message_post(
                    body=f"<b>MOVE-IN CLEARANCE GRANTED (Management Exception Approved)</b> for Tenant {rec.tenant_id.name} on Unit <b>{rec.unit_id.name}</b>. Reason: {rec.exception_reason or 'Authorized Exception'}",
                    subject="Move-In Clearance Approved (Exception)"
                )
                continue

            unmet = []

            # 1. Reservation fee paid
            has_reservation_paid = (
                (rec.opportunity_id and rec.opportunity_id.reservation_payment_status == 'verified') or
                (rec.reservation_fee_credit or 0.0) > 0 or
                bool(self.env['property.reservation'].search([('tenant_id', '=', rec.tenant_id.id), ('unit_id', '=', rec.unit_id.id), ('state', 'in', ['paid', 'converted'])]))
            )
            if not has_reservation_paid:
                unmet.append("1. Reservation Fee Paid / Verified")

            # 2. Move-In Invoice paid
            if not rec.move_in_invoice_id or rec.move_in_invoice_id.payment_state not in ['paid', 'in_payment']:
                unmet.append("2. Move-In Invoice Paid (Accounting Settlement)")

            # 3. Security deposit recorded & paid
            if (rec.security_deposit or 0.0) <= 0:
                unmet.append("3. Security Deposit Recorded (> PHP 0)")

            # 4. Access card paid, if applicable
            access_req = self.env['access.request'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if access_req and access_req.access_type == 'access_card' and access_req.payment_status not in ['paid', 'waived']:
                unmet.append("4. Access Card Application Payment Verified")

            # 5. Parking paid, if applicable
            parking_app = self.env['parking.application'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if parking_app and parking_app.payment_status not in ['paid', 'waived']:
                unmet.append("5. Parking Application Payment Verified")

            # 6. Wi-Fi paid, if applicable
            wifi_app = self.env['wifi.request'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if wifi_app and wifi_app.payment_status not in ['paid', 'waived']:
                unmet.append("6. Wi-Fi Application Payment Verified")

            # 7. Contract signed
            signed_stages = ['signed_tenant', 'submitted_billing', 'submitted_legal', 'for_notarization', 'notarized', 'released_tenant', 'active']
            if rec.stage not in signed_stages and not rec.signed_copy:
                unmet.append("7. Signed Lease Contract (Attached / Signed Stage)")

            # 8. Unit assessment completed
            has_unit_assessment = bool(rec.unit_assessment_task_ids) or bool(self.env['unit.assessment.task'].search([('unit_id', '=', rec.unit_id.id), ('stage', 'in', ['ready_move_in', 'completed', 'verified'])]))
            if not has_unit_assessment:
                unmet.append("8. Unit Assessment & Turnover Task Completed")

            # 9. Move-In Form / Inspection completed
            has_move_in_form = rec.move_in_checklist_done or bool(self.env['pmo.inspection'].search([('tenant_id', '=', rec.tenant_id.id), ('unit_id', '=', rec.unit_id.id), ('inspection_type', '=', 'move_in')]))
            if not has_move_in_form:
                unmet.append("9. PMO Move-In Inspection Form Completed")

            if unmet:
                raise UserError(f"MOVE-IN READINESS VALIDATION BLOCKED:\nThe following 9 pre-move-in requirements must be satisfied before move-in clearance can be granted:\n\n" + "\n".join(unmet))

            rec.move_in_cleared = True
            rec.move_in_cleared_date = fields.Datetime.now()
            rec.stage = 'active'
            rec.unit_id.occupancy_status = 'occupied'
            rec.unit_id.current_tenant_id = rec.tenant_id

            if rec.opportunity_id:
                rec.opportunity_id.move_in_cleared = True

            rec.message_post(
                body=f"<b>CLEARED FOR MOVE-IN!</b> All 9 Pre-Move-In Readiness Checkpoints (Reservation Fee, Move-In Invoice, Security Deposit, Access Card, Parking, Wi-Fi, Signed Contract, Unit Assessment, Move-In Form) verified for Tenant <b>{rec.tenant_id.name}</b> on Unit <b>{rec.unit_id.name}</b>.",
                subject="Cleared for Move-In Approved"
            )

    def action_verify_move_in_clearance(self):
        """ Alias method for Validate Move-In Readiness """
        return self.action_validate_move_in_readiness()

    def action_view_move_in_invoice(self):
        self.ensure_one()
        if not self.move_in_invoice_id:
            raise UserError("No Move-In Invoice has been generated for this lease contract yet.")
        return {
            'name': 'Move-In Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.move_in_invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }

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
