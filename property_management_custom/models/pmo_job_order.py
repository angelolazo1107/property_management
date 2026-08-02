# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class PMOJobOrder(models.Model):
    _name = 'pmo.job.order'
    _description = 'PMO Job Order & Maintenance Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Job Order Ref', required=True, copy=False, readonly=True, default='New')
    unit_id = fields.Many2one('product.product', string='Property Unit', domain="[('is_property_unit', '=', True)]", required=True)
    tenant_id = fields.Many2one('res.partner', string='Requesting Tenant / Dept', required=True)
    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', string='Originating Helpdesk Ticket')
    
    category = fields.Selection([
        ('plumbing', 'Plumbing Maintenance'),
        ('electrical', 'Electrical / Wiring'),
        ('hvac', 'Air Conditioning / HVAC'),
        ('carpentry', 'Carpentry & Structure'),
        ('janitorial', 'Cleaning & Sanitation'),
    ], string='Work Category', default='electrical', required=True)

    is_chargeable = fields.Boolean(string='Chargeable to Tenant', default=False)
    job_cost = fields.Monetary(string='Estimated Job Cost', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    
    payment_verified = fields.Boolean(string='Tenant Payment Verified (Accounting)', default=False)
    management_waiver_approved = fields.Boolean(string='Management Payment Waiver Approved', default=False)

    scheduled_date = fields.Datetime(string='MST Scheduled Date & Time')
    assigned_technician_id = fields.Many2one('res.users', string='Assigned MST Technician')

    stage = fields.Selection([
        ('intake', 'Helpdesk Intake'),
        ('admin_review', 'Admin Assessment'),
        ('tenant_approval', 'Pending Tenant Approval'),
        ('payment_pending', 'Pending Payment Check'),
        ('scheduled', 'MST Scheduled'),
        ('in_progress', 'Work In Progress'),
        ('completed', 'Work Completed'),
        ('closed', 'Closed & Invoiced'),
    ], string='Job Order Stage', default='intake', tracking=True)

    work_description = fields.Text(string='Problem Description & Scope of Work')
    completion_photos = fields.Binary(string='Completion Photo Evidence')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('pmo.job.order') or 'JO-0001'
        return super(PMOJobOrder, self).create(vals)

    def action_approve_waiver(self):
        for rec in self:
            rec.management_waiver_approved = True

    def action_schedule_mst(self):
        for rec in self:
            if rec.is_chargeable and not (rec.payment_verified or rec.management_waiver_approved):
                raise UserError("Cannot Schedule Work: Chargeable Job Order requires full payment verification before MST scheduling unless approved by Management waiver!")
            rec.stage = 'scheduled'
