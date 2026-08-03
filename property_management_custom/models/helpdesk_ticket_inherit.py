# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class HelpdeskTicketInherit(models.Model):
    _inherit = 'helpdesk.ticket'

    unit_id = fields.Many2one(
        'product.product',
        string='Property Unit',
        domain="[('is_property_unit', '=', True)]",
        tracking=True
    )
    lease_contract_id = fields.Many2one(
        'lease.contract',
        string='Lease Contract',
        tracking=True
    )
    pmo_job_order_ids = fields.One2many(
        'pmo.job.order',
        'helpdesk_ticket_id',
        string='PMO Job Orders'
    )
    pmo_job_order_count = fields.Integer(
        string='Job Orders Count',
        compute='_compute_pmo_job_order_count'
    )

    @api.depends('pmo_job_order_ids')
    def _compute_pmo_job_order_count(self):
        for rec in self:
            rec.pmo_job_order_count = len(rec.pmo_job_order_ids)

    @api.onchange('unit_id')
    def _onchange_unit_id(self):
        if self.unit_id:
            active_lease = self.env['lease.contract'].search([
                ('unit_id', '=', self.unit_id.id),
                ('stage', '=', 'active')
            ], limit=1)
            if active_lease:
                self.lease_contract_id = active_lease.id
                if not self.partner_id:
                    self.partner_id = active_lease.tenant_id.id

    def action_create_pmo_job_order(self):
        self.ensure_one()
        if not self.unit_id:
            raise UserError("Cannot create Job Order: Please assign a Property Unit to this Helpdesk Ticket first!")
        
        job_order_vals = {
            'unit_id': self.unit_id.id,
            'tenant_id': self.partner_id.id or self.env.user.partner_id.id,
            'helpdesk_ticket_id': self.id,
            'work_description': f"Helpdesk Ticket #{self.id}: {self.name}\n\nDescription: {self.description or 'N/A'}",
            'stage': 'intake',
        }
        job_order = self.env['pmo.job.order'].create(job_order_vals)

        self.message_post(
            body=f"🛠️ PMO Job Order <b>{job_order.name}</b> created for Unit <b>{self.unit_id.name}</b>.",
            subject="Job Order Created"
        )

        return {
            'name': 'PMO Job Order',
            'type': 'ir.actions.act_window',
            'res_model': 'pmo.job.order',
            'res_id': job_order.id,
            'view_mode': 'form',
            'target': 'current',
        }

    def action_view_pmo_job_orders(self):
        self.ensure_one()
        return {
            'name': 'PMO Job Orders',
            'type': 'ir.actions.act_window',
            'res_model': 'pmo.job.order',
            'view_mode': 'list,form',
            'domain': [('helpdesk_ticket_id', '=', self.id)],
            'context': {
                'default_helpdesk_ticket_id': self.id,
                'default_unit_id': self.unit_id.id if self.unit_id else False,
                'default_tenant_id': self.partner_id.id if self.partner_id else False,
            },
        }
