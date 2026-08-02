# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrderPropertyInherit(models.Model):
    _inherit = 'sale.order'

    target_unit_id = fields.Many2one(
        'product.product', 
        string='Target Property Unit', 
        domain="[('is_property_unit', '=', True)]", 
        tracking=True
    )
    intended_move_in_date = fields.Date(string='Intended Move-In Date')
    lease_term_months = fields.Integer(string='Lease Duration (Months)', default=12)

    reservation_fee_option = fields.Selection([
        ('5000', 'PHP 5,000 Standard Reservation Fee'),
        ('10000', 'PHP 10,000 Prime Unit Reservation Fee'),
        ('custom', 'Custom Amount'),
    ], string='Reservation Fee Structure', default='5000', tracking=True)

    reservation_fee_amount = fields.Monetary(
        string='Reservation Fee Amount', 
        currency_field='currency_id',
        default=5000.0,
        tracking=True
    )

    reservation_proof = fields.Binary(string='Proof of Payment (Reservation Deposit)')
    reservation_proof_filename = fields.Char(string='Payment Proof File Name')

    reservation_payment_status = fields.Selection([
        ('draft', 'Pending Reservation Deposit'),
        ('submitted', 'Proof Submitted to Billing'),
        ('verified', 'Payment Verified by Billing'),
        ('receipt_issued', 'Acknowledgement Receipt Issued'),
        ('refunded', 'Reservation Fee Released / Refunded'),
    ], string='Reservation Deposit Status', default='draft', tracking=True)

    acknowledgement_receipt_no = fields.Char(
        string='Acknowledgement Receipt (AR) Ref', 
        readonly=True, 
        copy=False, 
        tracking=True
    )

    @api.model
    def default_get(self, fields_list):
        res = super(SaleOrderPropertyInherit, self).default_get(fields_list)
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        if php_currency:
            res['currency_id'] = php_currency.id
            pricelist = self.env['product.pricelist'].search([('currency_id', '=', php_currency.id)], limit=1)
            if pricelist:
                res['pricelist_id'] = pricelist.id
        return res

    @api.onchange('partner_id')
    def _onchange_partner_id_set_php_currency(self):
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        if php_currency:
            self.currency_id = php_currency
            if not self.pricelist_id or self.pricelist_id.currency_id != php_currency:
                php_pricelist = self.env['product.pricelist'].search([('currency_id', '=', php_currency.id)], limit=1)
                if php_pricelist:
                    self.pricelist_id = php_pricelist

    @api.model_create_multi
    def create(self, vals_list):
        php_currency = self.env.ref('base.PHP', raise_if_not_found=False)
        php_pricelist = self.env['product.pricelist'].search([('currency_id', '=', php_currency.id)], limit=1) if php_currency else False
        for vals in vals_list:
            if php_currency:
                vals['currency_id'] = php_currency.id
                if php_pricelist and not vals.get('pricelist_id'):
                    vals['pricelist_id'] = php_pricelist.id
        return super(SaleOrderPropertyInherit, self).create(vals_list)

    @api.onchange('reservation_fee_option')
    def _onchange_reservation_fee_option(self):
        if self.reservation_fee_option == '5000':
            self.reservation_fee_amount = 5000.0
        elif self.reservation_fee_option == '10000':
            self.reservation_fee_amount = 10000.0

    @api.onchange('target_unit_id')
    def _onchange_target_unit_id(self):
        if self.target_unit_id and self.target_unit_id.list_price:
            # Auto update monthly rental lines if available
            for line in self.order_line:
                if line.product_id and line.product_id.name == 'Monthly Rental':
                    line.price_unit = self.target_unit_id.list_price

    def action_submit_reservation_proof(self):
        for rec in self:
            if not rec.reservation_proof:
                raise UserError("Please attach the Proof of Payment before submitting to Billing.")
            rec.reservation_payment_status = 'submitted'
            rec.message_post(
                body=f"Proof of Reservation Fee Payment ({rec.currency_id.symbol}{rec.reservation_fee_amount:,.2f}) has been submitted to Billing for verification.",
                subject="Reservation Payment Submitted"
            )

    def action_verify_reservation_payment(self):
        for rec in self:
            if rec.reservation_payment_status not in ['submitted', 'draft']:
                raise UserError("Reservation payment must be submitted or pending before verification.")
            
            rec.reservation_payment_status = 'verified'
            if not rec.acknowledgement_receipt_no:
                rec.acknowledgement_receipt_no = self.env['ir.sequence'].next_by_code('sale.order.acknowledgement.receipt') or f"AR-{rec.id:05d}"
            
            if rec.target_unit_id:
                rec.target_unit_id.occupancy_status = 'reserved'
                rec.target_unit_id.current_tenant_id = rec.partner_id

            if rec.opportunity_id:
                rec.opportunity_id.reservation_verified = True
                rec.opportunity_id.unit_hold_status = 'hold_active'
                rec.opportunity_id.official_receipt_no = rec.acknowledgement_receipt_no

            rec.message_post(
                body=f"Reservation Fee Payment of {rec.currency_id.symbol}{rec.reservation_fee_amount:,.2f} verified by Billing. Acknowledgement Receipt issued: <b>{rec.acknowledgement_receipt_no}</b>. Property Unit <b>{rec.target_unit_id.display_name if rec.target_unit_id else ''}</b> is now blocked / reserved.",
                subject="Payment Verified & Acknowledgement Receipt Issued"
            )

    def action_issue_acknowledgement_receipt(self):
        for rec in self:
            if rec.reservation_payment_status != 'verified':
                raise UserError("Payment must be verified by Billing before issuing Acknowledgement Receipt.")
            rec.reservation_payment_status = 'receipt_issued'
            rec.message_post(
                body=f"Official Acknowledgement Receipt <b>{rec.acknowledgement_receipt_no}</b> sent to Tenant {rec.partner_id.name}.",
                subject="Acknowledgement Receipt Issued"
            )


class SaleOrderTemplatePropertyInherit(models.Model):
    _inherit = 'sale.order.template'

    duration_value = fields.Integer(string='Duration Value', default=1)
    duration_unit = fields.Selection([
        ('day', 'Days'),
        ('week', 'Weeks'),
        ('month', 'Months'),
        ('year', 'Years'),
    ], string='Duration Unit', default='year')

