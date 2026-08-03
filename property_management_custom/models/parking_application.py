# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class ParkingApplication(models.Model):
    _name = 'parking.application'
    _description = 'Parking Application & Sticker Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Application Ref', 
        required=True, 
        copy=False, 
        readonly=True, 
        default='New'
    )
    tenant_id = fields.Many2one(
        'res.partner', 
        string='Tenant', 
        required=True, 
        tracking=True
    )
    unit_id = fields.Many2one(
        'product.product', 
        string='Unit', 
        domain="[('is_property_unit', '=', True)]", 
        required=True, 
        tracking=True
    )
    parking_type = fields.Selection([
        ('sapphire_parking', 'Sapphire Parking'),
        ('sapphire_sticker', 'Sapphire Sticker'),
        ('marina_sticker', 'Marina Sticker'),
    ], string='Parking Type', required=True, default='sapphire_parking', tracking=True)

    vehicle_type = fields.Selection([
        ('car', 'Car'),
        ('motorcycle', 'Motorcycle'),
    ], string='Vehicle Type', required=True, default='car', tracking=True)

    plate_number = fields.Char(
        string='Plate Number', 
        required=True, 
        tracking=True
    )

    or_attachment = fields.Binary(string='Official Receipt (OR) Attachment')
    or_attachment_filename = fields.Char(string='OR File Name')
    cr_attachment = fields.Binary(string='Certificate of Registration (CR) Attachment')
    cr_attachment_filename = fields.Char(string='CR File Name')
    drivers_license = fields.Binary(string='Driver’s License Attachment')
    drivers_license_filename = fields.Char(string='Driver License File Name')

    parking_fee = fields.Monetary(
        string='Parking Fee (PHP)', 
        currency_field='currency_id', 
        default=3000.0, 
        tracking=True
    )
    payment_status = fields.Selection([
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('waived', 'Waived'),
    ], string='Payment Status', default='unpaid', tracking=True)

    cashier_receipt = fields.Binary(string='Cashier Receipt / Proof of Payment')
    cashier_receipt_filename = fields.Char(string='Cashier Receipt File Name')
    invoice_id = fields.Many2one(
        'account.move', 
        string='Customer Invoice', 
        readonly=True, 
        copy=False
    )
    invoice_payment_state = fields.Selection(
        related='invoice_id.payment_state', 
        string='Invoice Payment Status'
    )

    assigned_parking_location = fields.Char(
        string='Assigned Parking Location (Slot / Area)', 
        tracking=True, 
        help="Specify assigned parking slot or designated area (e.g. B1 Slot 42)."
    )
    sticker_number = fields.Char(
        string='Issued Sticker Number', 
        tracking=True, 
        help="Specify the physical sticker number issued to the vehicle."
    )

    state = fields.Selection([
        ('draft', 'Draft'),
        ('for_payment', 'For Payment'),
        ('for_assignment', 'For Assignment'),
        ('active', 'Active Pass'),
        ('expired', 'Expired'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft', tracking=True)

    currency_id = fields.Many2one(
        'res.currency', 
        string='Currency', 
        default=lambda self: self.env.company.currency_id.id
    )
    notes = fields.Text(string='Notes / Remarks')

    def _validate_mandatory_documents(self):
        for rec in self:
            missing = []
            if not rec.plate_number:
                missing.append("Vehicle Plate Number")
            if not rec.or_attachment:
                missing.append("Official Receipt (OR) Attachment")
            if not rec.cr_attachment:
                missing.append("Certificate of Registration (CR) Attachment")
            if not rec.drivers_license:
                missing.append("Driver's License Attachment")
            
            if missing:
                raise UserError(f"Document Check Failed: Before submitting or approving the parking application, the following required items are missing: {', '.join(missing)}!")

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('parking.application') or 'PARK-2026-00001'
        return super(ParkingApplication, self).create(vals)

    def action_submit(self):
        for rec in self:
            rec._validate_mandatory_documents()
            rec.payment_status = 'unpaid'
            rec.state = 'for_payment'

            # Auto-create Customer Invoice if not exists
            if not rec.invoice_id:
                p_type_label = dict(rec._fields['parking_type'].selection).get(rec.parking_type)
                invoice_vals = {
                    'move_type': 'out_invoice',
                    'partner_id': rec.tenant_id.id,
                    'invoice_date': fields.Date.context_today(self),
                    'ref': f"Parking Application: {rec.name}",
                    'invoice_line_ids': [(0, 0, {
                        'name': f"Parking Pass Fee ({p_type_label}) - Plate: {rec.plate_number} [Unit: {rec.unit_id.name}]",
                        'quantity': 1,
                        'price_unit': rec.parking_fee or 0.0,
                    })],
                }
                invoice = self.env['account.move'].create(invoice_vals)
                rec.invoice_id = invoice.id

            rec.message_post(
                body=f"Parking Application <b>{rec.name}</b> submitted with all OR/CR & License documents. Customer Invoice <b>{rec.invoice_id.name or 'Draft Invoice'}</b> created for PHP {(rec.parking_fee or 0.0):,.2f}.",
                subject="Parking Application Submitted"
            )

    def action_validate_payment(self):
        for rec in self:
            rec._validate_mandatory_documents()
            rec.payment_status = 'paid'
            rec.state = 'for_assignment'
            rec.message_post(
                body=f"Payment of PHP {(rec.parking_fee or 0.0):,.2f} for Parking Application <b>{rec.name}</b> confirmed by Cashier. Advanced to For Assignment.",
                subject="Payment Validated"
            )

    def action_waive_payment(self):
        for rec in self:
            rec._validate_mandatory_documents()
            rec.payment_status = 'waived'
            rec.state = 'for_assignment'
            rec.message_post(
                body=f"Fee for Parking Application <b>{rec.name}</b> waived by Admin. Advanced to For Assignment.",
                subject="Payment Waived"
            )

    def action_activate_parking(self):
        for rec in self:
            rec._validate_mandatory_documents()
            if rec.payment_status not in ['paid', 'waived']:
                raise UserError("Cannot release parking assignment: Payment status is Unpaid! Cashier must confirm payment before parking assignment can be activated.")
            if not rec.assigned_parking_location:
                raise UserError("Please enter the Assigned Parking Location (Slot / Area) before releasing/activating the parking application!")

            rec.state = 'active'

            # 1. Update Move-In Record
            inspection = self.env['pmo.inspection'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id),
                ('inspection_type', '=', 'move_in')
            ], limit=1)
            if inspection:
                inspection.wifi_parking_assigned = True
                if rec.sticker_number:
                    inspection.stickers_count = (inspection.stickers_count or 0) + 1
                inspection.message_post(
                    body=f"Parking Slot Assigned for Tenant <b>{rec.tenant_id.name}</b>. Location: <b>{rec.assigned_parking_location}</b> | Sticker: <b>{rec.sticker_number or 'N/A'}</b> | Plate: <b>{rec.plate_number}</b>.",
                    subject="Parking Assignment Synced to Move-In Inspection"
                )

            # 2. Integrate with Lease Contract for Recurring Monthly Billing
            lease = self.env['lease.contract'].search([
                ('tenant_id', '=', rec.tenant_id.id),
                ('unit_id', '=', rec.unit_id.id),
                ('stage', 'in', ['active', 'released_tenant', 'notarized'])
            ], limit=1)
            if lease:
                lease.parking_fee = rec.parking_fee
                lease.message_post(
                    body=f"Parking Pass Activated ({rec.name}). Assigned Slot: <b>{rec.assigned_parking_location}</b> | Plate: <b>{rec.plate_number}</b>. Monthly Parking Fee of PHP {(rec.parking_fee or 0.0):,.2f} added to Lease Contract recurring billing.",
                    subject="Parking Fee Added to Monthly Lease Billing"
                )

            rec.message_post(
                body=f"Parking Application <b>{rec.name}</b> Activated & Released. Assigned Slot: <b>{rec.assigned_parking_location}</b> | Sticker Number: <b>{rec.sticker_number or 'N/A'}</b> | Plate Number: <b>{rec.plate_number}</b>.",
                subject="Parking Slot Released & Activated"
            )

    def action_expire(self):
        for rec in self:
            rec.state = 'expired'
            rec.message_post(
                body=f"Parking Application <b>{rec.name}</b> marked as Expired.",
                subject="Parking Pass Expired"
            )

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'
            rec.message_post(
                body=f"Parking Application <b>{rec.name}</b> cancelled.",
                subject="Application Cancelled"
            )

    def action_view_invoice(self):
        self.ensure_one()
        if not self.invoice_id:
            raise UserError("No invoice has been generated for this parking application yet.")
        return {
            'name': 'Customer Invoice',
            'type': 'ir.actions.act_window',
            'res_model': 'account.move',
            'res_id': self.invoice_id.id,
            'view_mode': 'form',
            'target': 'current',
        }
