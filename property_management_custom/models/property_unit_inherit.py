# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductProductPropertyInherit(models.Model):
    _inherit = 'product.product'

    is_property_unit = fields.Boolean(string='Is Property Unit / Commercial Space', default=True)
    building_id = fields.Many2one('x_buildings', string='Building / Property Complex', tracking=True)
    floor_level = fields.Char(string='Floor Level')
    area_sqm = fields.Float(string='Floor Area (sqm)', digits=(16, 2))
    
    active_lease_ids = fields.One2many('lease.contract', 'unit_id', string='Lease Contracts')
    
    occupancy_status = fields.Selection([
        ('available', 'Available'),
        ('reserved', 'Reserved'),
        ('occupied', 'Occupied'),
        ('vacated', 'Vacated / Turnover'),
        ('under_repair', 'Under Repair'),
        ('under_cleaning', 'Under Cleaning'),
        ('maintenance', 'Under Maintenance'),
        ('blocked', 'Blocked / Out of Service'),
    ], string='Occupancy Status', compute='_compute_occupancy_status', store=True, readonly=False, tracking=True)

    @api.depends('active_lease_ids.stage', 'active_lease_ids.date_start', 'active_lease_ids.date_end')
    def _compute_occupancy_status(self):
        today = fields.Date.today()
        for rec in self:
            if not rec.is_property_unit:
                continue
            active_contract = self.env['lease.contract'].search([
                ('unit_id', '=', rec.id),
                ('stage', 'in', ['active', 'for_renewal', 'renewal_offered', 'renewed', 'for_move_out', 'signed_tenant', 'notarized', 'released_tenant']),
                ('date_start', '<=', today),
                ('date_end', '>=', today),
            ], order='date_end desc', limit=1)
            
            if active_contract:
                rec.occupancy_status = 'occupied'
                rec.current_tenant_id = active_contract.tenant_id.id
            else:
                active_res = self.env['property.reservation'].search([
                    ('unit_id', '=', rec.id),
                    ('state', 'in', ['draft', 'submitted', 'confirmed']),
                ], limit=1)
                if active_res:
                    rec.occupancy_status = 'reserved'
                    rec.current_tenant_id = active_res.partner_id.id
                elif rec.occupancy_status in ('occupied', 'reserved'):
                    rec.occupancy_status = 'available'
                    rec.current_tenant_id = False
                elif not rec.occupancy_status:
                    rec.occupancy_status = 'available'

    property_type = fields.Selection([
        ('commercial', 'Commercial Retail'),
        ('office', 'Office Suite'),
        ('residential_studio', 'Residential Studio'),
        ('residential_1br', 'Residential 1-Bedroom'),
        ('residential_2br', 'Residential 2-Bedroom'),
        ('residential_penthouse', 'Executive Penthouse'),
        ('warehouse', 'Industrial Warehouse'),
    ], string='Property Type', default='residential_studio', tracking=True)

    property_address = fields.Char(string='Property Full Address', tracking=True)

    current_tenant_id = fields.Many2one('res.partner', string='Current Tenant', tracking=True)
    electricity_meter_no = fields.Char(string='Electricity Meter ID')
    water_meter_no = fields.Char(string='Water Meter ID')
    latest_electric_reading = fields.Float(string='Latest Electric Reading (kWh)')
    latest_water_reading = fields.Float(string='Latest Water Reading (cbm)')

    @api.depends('name', 'default_code', 'is_property_unit', 'occupancy_status', 'floor_level', 'building_id')
    def _compute_display_name(self):
        super()._compute_display_name()
        status_dict = {
            'available': 'Available',
            'reserved': 'Reserved',
            'occupied': 'Occupied',
            'vacated': 'Vacated',
            'under_repair': 'Under Repair',
            'under_cleaning': 'Under Cleaning',
            'maintenance': 'Maintenance',
            'blocked': 'Blocked',
        }
        for rec in self:
            if rec.is_property_unit or rec.occupancy_status:
                status_label = status_dict.get(rec.occupancy_status, 'Available')
                details = []
                if rec.floor_level:
                    details.append(rec.floor_level)
                if status_label:
                    details.append(f"[{status_label.upper()}]")
                if rec.list_price and rec.list_price > 0:
                    details.append(f"₱{rec.list_price:,.2f}")
                
                if details:
                    rec.display_name = f"{rec.name} — {' · '.join(details)}"
                else:
                    rec.display_name = rec.name


class ResCompanyCurrencyFix(models.Model):
    _inherit = 'res.company'

    def write(self, vals):
        if 'currency_id' in vals:
            currency_id = vals['currency_id']
            for company in self:
                if currency_id and company.currency_id.id != currency_id:
                    self.env.cr.execute(
                        "UPDATE res_company SET currency_id = %s WHERE id = %s",
                        (currency_id, company.id)
                    )
                    company.invalidate_recordset(['currency_id'])
            vals_copy = dict(vals)
            vals_copy.pop('currency_id', None)
            return super(ResCompanyCurrencyFix, self).write(vals_copy)
        return super(ResCompanyCurrencyFix, self).write(vals)


class AccountAnalyticAccountPropertyInherit(models.Model):
    _inherit = 'account.analytic.account'

    x_is_property = fields.Boolean(string='Is Property', default=False)
    x_property_building_id = fields.Many2one('x_buildings', string='Building')
    x_rental_contract_id = fields.Many2one('sale.order', string='Rental Contract')

