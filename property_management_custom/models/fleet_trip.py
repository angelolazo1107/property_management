# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetTripRequest(models.Model):
    _name = 'fleet.trip.request'
    _description = 'Vehicle Request and Driver Trip Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Trip Request Ref', required=True, copy=False, readonly=True, default='New')
    vehicle_id = fields.Many2one('fleet.vehicle', string='Assigned Vehicle', required=True)
    driver_id = fields.Many2one('res.partner', string='Assigned Driver', required=True)
    
    passenger_name = fields.Char(string='Passenger / Department', required=True)
    purpose = fields.Selection([
        ('errand', 'Internal Company Errand'),
        ('guest_transport', 'Tenant / Guest Transport'),
        ('inspection', 'Property Site Inspection'),
        ('maintenance', 'Maintenance Dispatch'),
    ], string='Trip Purpose', default='errand', required=True)

    is_chargeable = fields.Boolean(string='Chargeable Trip to Tenant', default=False)
    chargeable_tenant_id = fields.Many2one('res.partner', string='Chargeable Tenant Account')
    trip_fee = fields.Monetary(string='Calculated Trip Fee', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)

    mileage_start = fields.Integer(string='Odometer Start (km)', required=True)
    mileage_end = fields.Integer(string='Odometer End (km)')
    total_km = fields.Integer(string='Total Distance (km)', compute='_compute_km', store=True)

    status = fields.Selection([
        ('draft', 'Trip Requested'),
        ('approved', 'Admin Approved'),
        ('in_progress', 'Trip In Progress'),
        ('completed', 'Trip Completed'),
        ('verified', 'Accounting Verified'),
    ], string='Status', default='draft', tracking=True)

    @api.depends('mileage_start', 'mileage_end')
    def _compute_km(self):
        for rec in self:
            if rec.mileage_end and rec.mileage_start:
                rec.total_km = max(0, rec.mileage_end - rec.mileage_start)
            else:
                rec.total_km = 0

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('fleet.trip.request') or 'TRIP-0001'
        return super(FleetTripRequest, self).create(vals)

    def action_complete_trip(self):
        for rec in self:
            rec.status = 'completed'

    def action_verify_trip(self):
        for rec in self:
            rec.status = 'verified'
