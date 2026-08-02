# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CrmLeadInherit(models.Model):
    _inherit = 'crm.lead'

    target_unit_id = fields.Many2one('product.product', string='Target Unit / Property', domain="[('is_property_unit', '=', True)]")
    intended_move_in_date = fields.Date(string='Intended Move-In Date')
    preferred_budget = fields.Monetary(string='Preferred Rent Budget', currency_field='company_currency')
    
    parking_required = fields.Boolean(string='Parking Requirement')
    wifi_required = fields.Boolean(string='Wi-Fi Connection Requirement')
    pet_details = fields.Char(string='Pet Details / Registration')
    broker_id = fields.Many2one('res.partner', string='Assigned Broker / Agent')
    
    # Stage 2 Ocular Visit Integration
    ocular_visit_ids = fields.One2many('ocular.visit', 'lead_id', string='Ocular Visit Records')
    ocular_visit_count = fields.Integer(string='Ocular Visits Count', compute='_compute_ocular_visit_count')

    ocular_visit_date = fields.Datetime(string='Next Ocular Visit Schedule')
    security_visitor_details = fields.Text(string='Visitor Security Details (For Gate Pass)')
    ocular_status = fields.Selection([
        ('pending', 'Pending Schedule'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Visit Completed'),
        ('rescheduled', 'Rescheduled'),
        ('cancelled', 'Cancelled'),
    ], string='Ocular Visit Status', default='pending', tracking=True)

    bis_status = fields.Selection([
        ('draft', 'Not Submitted'),
        ('submitted', 'BIS Submitted'),
        ('verified', 'BIS Verified'),
        ('rejected', 'BIS Rejected'),
    ], string='BIS (Tenant Info Sheet)', default='draft', tracking=True)

    reservation_proof = fields.Binary(string='Reservation Deposit Proof')
    reservation_proof_name = fields.Char(string='File Name')
    reservation_verified = fields.Boolean(string='Accounting Verified Payment', tracking=True)
    official_receipt_no = fields.Char(string='Official Receipt (OR) Ref')
    unit_hold_status = fields.Selection([
        ('none', 'No Hold'),
        ('hold_active', 'Unit Blocked / On Hold'),
        ('released', 'Hold Released'),
    ], string='Unit Blocking Status', default='none', tracking=True)

    legal_clearance = fields.Boolean(string='Legal Clearance Approved', tracking=True)
    move_in_cleared = fields.Boolean(string='Move-In Financial Clearance Granted', tracking=True)

    # Stage 3 Quotation & Reservation Integration
    property_quotation_ids = fields.One2many('sale.order', 'opportunity_id', string='Leasing Quotations')
    property_quotation_count = fields.Integer(string='Quotations Count', compute='_compute_property_quotation_count')

    property_reservation_ids = fields.One2many('property.reservation', 'opportunity_id', string='Unit Reservations')
    property_reservation_count = fields.Integer(string='Reservations Count', compute='_compute_property_reservation_count')

    bis_application_ids = fields.One2many('tenant.application.bis', 'opportunity_id', string='BIS Applications')
    bis_application_count = fields.Integer(string='BIS Count', compute='_compute_bis_application_count')

    @api.depends('bis_application_ids')
    def _compute_bis_application_count(self):
        for rec in self:
            rec.bis_application_count = len(rec.bis_application_ids)

    def action_view_bis(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_tenant_application_bis")
        action['domain'] = [('opportunity_id', '=', self.id)]
        action['context'] = {
            'default_opportunity_id': self.id,
            'default_tenant_id': self.partner_id.id if self.partner_id else False,
            'default_unit_id': self.target_unit_id.id if self.target_unit_id else False,
            'default_move_in_date': self.intended_move_in_date,
        }
        return action

    def action_create_bis(self):
        self.ensure_one()
        if not self.partner_id:
            partner_vals = {
                'name': self.contact_name or self.partner_name or self.name,
                'email': self.email_from,
                'phone': self.phone or self.mobile,
                'is_company': False if self.contact_name else True,
            }
            partner = self.env['res.partner'].create(partner_vals)
            self.partner_id = partner.id

        bis_vals = {
            'tenant_id': self.partner_id.id,
            'unit_id': self.target_unit_id.id if self.target_unit_id else False,
            'opportunity_id': self.id,
            'move_in_date': self.intended_move_in_date,
            'with_agent': True if self.broker_id else False,
            'agent_id': self.broker_id.id if self.broker_id else False,
        }
        bis = self.env['tenant.application.bis'].create(bis_vals)
        if self.target_unit_id:
            bis._onchange_unit_id()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Tenant Application / BIS',
            'res_model': 'tenant.application.bis',
            'res_id': bis.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.depends('property_reservation_ids')
    def _compute_property_reservation_count(self):
        for rec in self:
            rec.property_reservation_count = len(rec.property_reservation_ids)

    def action_view_reservations(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_property_reservation")
        action['domain'] = [('opportunity_id', '=', self.id)]
        action['context'] = {
            'default_opportunity_id': self.id,
            'default_tenant_id': self.partner_id.id if self.partner_id else False,
            'default_unit_id': self.target_unit_id.id if self.target_unit_id else False,
        }
        return action

    @api.depends('property_quotation_ids')
    def _compute_property_quotation_count(self):
        for rec in self:
            rec.property_quotation_count = len(rec.property_quotation_ids)

    def action_view_quotations(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("sale.action_quotations_with_onboarding")
        action['domain'] = [('opportunity_id', '=', self.id)]
        action['context'] = {
            'default_opportunity_id': self.id,
            'default_partner_id': self.partner_id.id if self.partner_id else False,
            'default_target_unit_id': self.target_unit_id.id if self.target_unit_id else False,
            'default_intended_move_in_date': self.intended_move_in_date,
        }
        return action

    def action_create_quotation(self):
        self.ensure_one()
        if not self.partner_id:
            # Auto-create or require partner
            partner_vals = {
                'name': self.contact_name or self.partner_name or self.name,
                'email': self.email_from,
                'phone': self.phone or self.mobile,
                'is_company': False if self.contact_name else True,
            }
            partner = self.env['res.partner'].create(partner_vals)
            self.partner_id = partner.id

        # Determine best quotation template based on requirements
        template_xml_id = 'property_management_custom.template_bare_unit_rental'
        if self.parking_required:
            template_xml_id = 'property_management_custom.template_rental_with_parking'
        elif self.wifi_required:
            template_xml_id = 'property_management_custom.template_rental_with_wifi'
        elif self.pet_details:
            template_xml_id = 'property_management_custom.template_rental_with_pet'

        template = self.env.ref(template_xml_id, raise_if_not_found=False)

        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        php_pricelist = self.env['product.pricelist'].search([('currency_id', '=', php_currency.id)], limit=1) if php_currency else False

        so_vals = {
            'partner_id': self.partner_id.id,
            'opportunity_id': self.id,
            'target_unit_id': self.target_unit_id.id if self.target_unit_id else False,
            'intended_move_in_date': self.intended_move_in_date,
            'sale_order_template_id': template.id if template else False,
            'currency_id': php_currency.id if php_currency else False,
            'pricelist_id': php_pricelist.id if php_pricelist else False,
        }

        sale_order = self.env['sale.order'].create(so_vals)
        if template:
            sale_order._onchange_sale_order_template_id()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Leasing Quotation',
            'res_model': 'sale.order',
            'res_id': sale_order.id,
            'view_mode': 'form',
            'target': 'current',
        }

    @api.depends('ocular_visit_ids')
    def _compute_ocular_visit_count(self):
        for rec in self:
            rec.ocular_visit_count = len(rec.ocular_visit_ids)

    def action_view_ocular_visits(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("property_management_custom.action_ocular_visit")
        action['domain'] = [('lead_id', '=', self.id)]
        action['context'] = {
            'default_lead_id': self.id,
            'default_visitor_name': self.contact_name or self.partner_name or self.name,
            'default_contact_number': self.phone or self.mobile,
            'default_agent_id': self.user_id.id if self.user_id else self.env.uid,
        }
        return action

    def action_schedule_ocular(self):
        for rec in self:
            rec.ocular_status = 'scheduled'

    def action_complete_ocular(self):
        for rec in self:
            rec.ocular_status = 'completed'

    def action_verify_bis(self):
        for rec in self:
            rec.bis_status = 'verified'

    def action_verify_reservation_payment(self):
        for rec in self:
            rec.reservation_verified = True
            rec.unit_hold_status = 'hold_active'
            if rec.target_unit_id:
                rec.target_unit_id.occupancy_status = 'reserved'

    def action_verify_move_in_clearance(self):
        for rec in self:
            rec.move_in_cleared = True

