# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class UnitAssessmentTask(models.Model):
    _name = 'unit.assessment.task'
    _description = 'Unit Assessment and Turnover Task (SARA Replacement)'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Assessment Task Number', required=True, copy=False, readonly=True, default='New')
    unit_id = fields.Many2one(
        'product.product', 
        string='Property Unit Number', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    tenant_id = fields.Many2one('res.partner', string='Tenant / Client Name', tracking=True)
    lease_contract_id = fields.Many2one('lease.contract', string='Associated Lease Contract')
    opportunity_id = fields.Many2one('crm.lead', string='Associated CRM Opportunity')

    admin_user_id = fields.Many2one('res.users', string='Assigned Admin Staff', tracking=True)
    housekeeping_user_id = fields.Many2one('res.users', string='Assigned Housekeeping Lead', tracking=True)
    inspection_date = fields.Date(string='Inspection Date', default=fields.Date.context_today, tracking=True)

    stage = fields.Selection([
        ('request_created', 'Request Created'),
        ('assigned_admin', 'Assigned to Admin'),
        ('assigned_housekeeping', 'Assigned to Housekeeping'),
        ('inspection_ongoing', 'Inspection Ongoing'),
        ('cleaning_required', 'Cleaning Required'),
        ('repair_required', 'Repair Required'),
        ('completed', 'Completed'),
        ('ready_move_in', 'Ready for Move-In'),
    ], string='Task Stage', default='request_created', tracking=True)

    overall_assessment_result = fields.Selection([
        ('pending', 'Pending Inspection'),
        ('passed', 'Passed - Ready for Move-In'),
        ('failed', 'Failed - Action Required'),
    ], string='Assessment Result', default='pending', tracking=True)

    # 11-Point Assessment Checklist Items
    unit_cleanliness_checked = fields.Boolean(string='Unit cleanliness checked', default=False, tracking=True)
    no_existing_damage_confirmed = fields.Boolean(string='No existing damage confirmed', default=False, tracking=True)
    lights_working = fields.Boolean(string='Lights working', default=False, tracking=True)
    ac_checked = fields.Boolean(string='Air-conditioning checked', default=False, tracking=True)
    plumbing_checked = fields.Boolean(string='Plumbing checked', default=False, tracking=True)
    door_lock_checked = fields.Boolean(string='Door lock checked', default=False, tracking=True)
    windows_checked = fields.Boolean(string='Windows checked', default=False, tracking=True)
    
    is_furnished_unit = fields.Boolean(string='Is Furnished Unit', default=False)
    furniture_checked = fields.Boolean(string='Furniture checked', default=False, tracking=True)

    pre_move_in_photos = fields.Binary(string='Pre-Move-In Photos Upload')
    pre_move_in_photos_filename = fields.Char(string='Photo File Name')

    admin_approval = fields.Boolean(string='Admin Approval Sign-Off', default=False, tracking=True)
    housekeeping_approval = fields.Boolean(string='Housekeeping Approval Sign-Off', default=False, tracking=True)

    notes = fields.Text(string='Inspection Findings & Assessment Notes')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('unit.assessment.task') or 'ASSESS-2026-00001'
        return super(UnitAssessmentTask, self).create(vals_list)

    def action_assign_admin(self):
        for rec in self:
            rec.stage = 'assigned_admin'
            rec.message_post(body=f"Assessment Task <b>{rec.name}</b> assigned to Admin Team.", subject="Assigned to Admin")

    def action_assign_housekeeping(self):
        for rec in self:
            rec.stage = 'assigned_housekeeping'
            rec.message_post(body=f"Assessment Task <b>{rec.name}</b> assigned to Housekeeping Team.", subject="Assigned to Housekeeping")

    def action_start_inspection(self):
        for rec in self:
            rec.stage = 'inspection_ongoing'
            rec.message_post(body=f"Inspection ongoing for Property Unit <b>{rec.unit_id.display_name}</b>.", subject="Inspection Ongoing")

    def action_pass_assessment(self):
        for rec in self:
            # Check required checklist items
            missing = []
            if not rec.unit_cleanliness_checked:
                missing.append("Unit cleanliness checked")
            if not rec.no_existing_damage_confirmed:
                missing.append("No existing damage confirmed")
            if not rec.lights_working:
                missing.append("Lights working")
            if not rec.ac_checked:
                missing.append("Air-conditioning checked")
            if not rec.plumbing_checked:
                missing.append("Plumbing checked")
            if not rec.door_lock_checked:
                missing.append("Door lock checked")
            if not rec.windows_checked:
                missing.append("Windows checked")
            if rec.is_furnished_unit and not rec.furniture_checked:
                missing.append("Furniture checked")
            
            if missing:
                raise UserError("Assessment Clearance Blocked:\nThe following required checklist items must be checked off before passing:\n• " + "\n• ".join(missing))

            if not rec.admin_approval or not rec.housekeeping_approval:
                raise UserError("Approval Required: Both Admin Approval and Housekeeping Approval sign-offs are required before setting Unit as Ready for Move-In!")

            rec.overall_assessment_result = 'passed'
            rec.stage = 'ready_move_in'
            
            if rec.unit_id:
                rec.unit_id.occupancy_status = 'available'

            if rec.lease_contract_id:
                rec.lease_contract_id.move_in_checklist_done = True

            rec.message_post(
                body=f"Unit Assessment <b>{rec.name}</b> PASSED. Both Admin and Housekeeping approvals verified. Property Unit <b>{rec.unit_id.display_name}</b> is now <b>Ready for Move-In</b>.",
                subject="Unit Assessment Passed & Ready for Move-In"
            )

    def action_require_cleaning(self):
        for rec in self:
            rec.overall_assessment_result = 'failed'
            rec.stage = 'cleaning_required'
            if rec.unit_id:
                rec.unit_id.occupancy_status = 'under_cleaning'
            rec.message_post(
                body=f"Unit Assessment <b>{rec.name}</b> marked FAILED - Cleaning Required. Property Unit <b>{rec.unit_id.display_name}</b> status updated to <b>Under Cleaning</b>.",
                subject="Cleaning Required"
            )

    def action_require_repair(self):
        for rec in self:
            rec.overall_assessment_result = 'failed'
            rec.stage = 'repair_required'
            if rec.unit_id:
                rec.unit_id.occupancy_status = 'under_repair'
            rec.message_post(
                body=f"Unit Assessment <b>{rec.name}</b> marked FAILED - Repair Required. Property Unit <b>{rec.unit_id.display_name}</b> status updated to <b>Under Repair</b>.",
                subject="Repair Required"
            )
