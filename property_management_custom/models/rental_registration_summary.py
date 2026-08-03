# -*- coding: utf-8 -*-
from odoo import models, fields, api

class RentalRegistrationSummary(models.Model):
    _name = 'rental.registration.summary'
    _description = 'Rental Registration Summary & SSP Posting'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Registration Ref', 
        required=True, 
        copy=False, 
        readonly=True, 
        default='New'
    )
    tenant_id = fields.Many2one(
        'res.partner', 
        string='Tenant Name', 
        required=True, 
        tracking=True
    )
    unit_id = fields.Many2one(
        'product.product', 
        string='Unit Number', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    lease_contract_id = fields.Many2one(
        'lease.contract', 
        string='Lease Contract Reference', 
        tracking=True
    )
    move_in_form_id = fields.Many2one(
        'move.in.form', 
        string='Move-In Form Reference', 
        tracking=True
    )

    furniture_package = fields.Char(
        string='Furniture Package', 
        tracking=True, 
        help="Specify furniture configuration (e.g. Fully Furnished, Semi-Furnished, Executive Package)."
    )
    move_in_date = fields.Date(
        string='Move-In Date', 
        required=True, 
        default=fields.Date.context_today, 
        tracking=True
    )
    lease_period = fields.Char(
        string='Lease Period', 
        tracking=True, 
        help="e.g. Aug 1, 2026 to Jul 31, 2027 (12 Months)."
    )

    deposit_amount = fields.Monetary(
        string='Deposit Amount', 
        currency_field='currency_id', 
        tracking=True
    )
    rental_amount = fields.Monetary(
        string='Rental Amount', 
        currency_field='currency_id', 
        tracking=True
    )

    agent_id = fields.Many2one(
        'res.partner', 
        string='Agent / Broker Name', 
        tracking=True
    )

    wifi_info = fields.Text(
        string='Wi-Fi Information', 
        tracking=True, 
        help="Wi-Fi SSID, Password, Plan details, and Router Serial."
    )
    parking_info = fields.Text(
        string='Parking Information', 
        tracking=True, 
        help="Assigned parking slot/area, sticker number, and vehicle plate."
    )

    other_notes = fields.Text(string='Other Notes / Manual Remarks')

    posted_to_sales_group = fields.Boolean(
        string='Posted to SSP Leasing Sales Group', 
        default=False, 
        tracking=True
    )
    posted_date = fields.Datetime(
        string='Posted Timestamp', 
        readonly=True
    )

    state = fields.Selection([
        ('draft', 'Draft Summary'),
        ('generated', 'Summary Compiled'),
        ('posted', 'Posted to SSP Sales Group'),
    ], string='Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )

    @api.onchange('lease_contract_id')
    def _onchange_lease_contract_id(self):
        if self.lease_contract_id:
            self.tenant_id = self.lease_contract_id.tenant_id
            self.unit_id = self.lease_contract_id.unit_id
            self.rental_amount = self.lease_contract_id.monthly_rent
            self.deposit_amount = self.lease_contract_id.security_deposit
            self.lease_period = f"{self.lease_contract_id.date_start} to {self.lease_contract_id.date_end} ({self.lease_contract_id.contract_term_months} Months)"
            self.furniture_package = "Fully Furnished Package" if (self.lease_contract_id.furniture_rental_fee or 0.0) > 0 else "Standard Unit Package"

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('rental.registration.summary') or 'RREG-2026-00001'
        return super(RentalRegistrationSummary, self).create(vals)

    def action_generate_summary(self):
        for rec in self:
            # 1. Compile Lease Terms if linked
            if rec.lease_contract_id:
                rec.tenant_id = rec.lease_contract_id.tenant_id
                rec.unit_id = rec.lease_contract_id.unit_id
                rec.rental_amount = rec.lease_contract_id.monthly_rent
                rec.deposit_amount = rec.lease_contract_id.security_deposit
                rec.lease_period = f"{rec.lease_contract_id.date_start} to {rec.lease_contract_id.date_end} ({rec.lease_contract_id.contract_term_months} Months)"
                if not rec.furniture_package:
                    rec.furniture_package = "Fully Furnished Package" if (rec.lease_contract_id.furniture_rental_fee or 0.0) > 0 else "Standard Unit Package"

            # 2. Compile Move-In Date if linked
            if rec.move_in_form_id and rec.move_in_form_id.move_in_date:
                rec.move_in_date = rec.move_in_form_id.move_in_date

            # 3. Compile Agent Info
            commission_claim = self.env['agent.commission'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if commission_claim:
                rec.agent_id = commission_claim.agent_id

            # 4. Compile Wi-Fi Info
            wifi_req = self.env['wifi.request'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if wifi_req:
                rec.wifi_info = f"Plan: {wifi_req.plan_type.title()} | SSID: {wifi_req.wifi_username or 'Pending'} | Router SN: {wifi_req.router_serial or 'N/A'}"

            # 5. Compile Parking Info
            parking_app = self.env['parking.application'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id)
            ], limit=1)
            if parking_app:
                rec.parking_info = f"Type: {parking_app.parking_type.replace('_', ' ').title()} | Slot: {parking_app.assigned_parking_location or 'N/A'} | Sticker: {parking_app.sticker_number or 'N/A'} | Plate: {parking_app.plate_number}"

            rec.state = 'generated'
            rec.message_post(
                body=f"Rental Registration Summary <b>{rec.name}</b> compiled for Tenant <b>{rec.tenant_id.name}</b> on Unit <b>{rec.unit_id.name}</b>.",
                subject="Rental Registration Summary Compiled"
            )

    def action_post_to_sales_group(self):
        for rec in self:
            rec.posted_to_sales_group = True
            rec.posted_date = fields.Datetime.now()
            rec.state = 'posted'

            broadcast_card = (
                f"📢 <b>SSP LEASING SALES GROUP - RENTAL REGISTRATION BROADCAST</b><br/><br/>"
                f"👤 <b>Tenant Name:</b> {rec.tenant_id.name}<br/>"
                f"🏢 <b>Unit Number:</b> {rec.unit_id.name}<br/>"
                f"🛋️ <b>Furniture Package:</b> {rec.furniture_package or 'N/A'}<br/>"
                f"📅 <b>Move-In Date:</b> {rec.move_in_date}<br/>"
                f"⏳ <b>Lease Period:</b> {rec.lease_period or 'N/A'}<br/>"
                f"💰 <b>Security Deposit:</b> PHP {(rec.deposit_amount or 0.0):,.2f}<br/>"
                f"💵 <b>Monthly Rent:</b> PHP {(rec.rental_amount or 0.0):,.2f}<br/>"
                f"👔 <b>Agent / Broker:</b> {rec.agent_id.name if rec.agent_id else 'In-House Leasing'}<br/>"
                f"📶 <b>Wi-Fi Info:</b> {rec.wifi_info or 'N/A'}<br/>"
                f"🚗 <b>Parking Info:</b> {rec.parking_info or 'N/A'}<br/>"
                f"📝 <b>Other Notes:</b> {rec.other_notes or 'None'}<br/>"
            )

            rec.message_post(body=broadcast_card, subject="Posted to SSP Leasing Sales Group")
