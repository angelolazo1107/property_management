# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyBuilding(models.Model):
    _name = 'property.building'
    _description = 'Property Building / Real Estate Complex'
    _order = 'name asc'

    name = fields.Char(string='Building / Tower Name', required=True, tracking=True)
    code = fields.Char(string='Building Code', copy=False)
    address = fields.Text(string='Building Address')
    total_floors = fields.Integer(string='Total Floor Levels', default=1)
    
    unit_ids = fields.One2many('product.product', 'building_id', string='Property Units')
    unit_count = fields.Integer(string='Total Units Count', compute='_compute_unit_count')

    active = fields.Boolean(string='Active', default=True)

    @api.depends('unit_ids')
    def _compute_unit_count(self):
        for rec in self:
            rec.unit_count = len(rec.unit_ids)

    @api.model
    def _register_hook(self):
        super()._register_hook()
        try:
            # 1. Clean up dummy buildings
            self.env.cr.execute("""
                DELETE FROM property_building 
                WHERE name IN (
                    'Alon Tower 1 - Residential & Commercial',
                    'Haraya Executive Residences',
                    'Aura Commercial & Retail Strip'
                );
            """)

            # 2. Ensure the 3 real Enterprise Buildings exist
            self.env.cr.execute("""
                INSERT INTO property_building (name, code, address, total_floors, active, create_date, write_date)
                SELECT 'Park Station', 'PST-01', 'Rue de Bruxelles 119 1083 Louise', 12, true, NOW(), NOW()
                WHERE NOT EXISTS (SELECT 1 FROM property_building WHERE name = 'Park Station');

                INSERT INTO property_building (name, code, address, total_floors, active, create_date, write_date)
                SELECT 'Immeuble Bellevue', 'IBV-02', 'Avenue du Chateau 123 1400 Uccle', 8, true, NOW(), NOW()
                WHERE NOT EXISTS (SELECT 1 FROM property_building WHERE name = 'Immeuble Bellevue');

                INSERT INTO property_building (name, code, address, total_floors, active, create_date, write_date)
                SELECT 'Ferme Saint-Jean', 'FSJ-03', 'Rue de Neupré 108 8934 Osivies', 5, true, NOW(), NOW()
                WHERE NOT EXISTS (SELECT 1 FROM property_building WHERE name = 'Ferme Saint-Jean');
            """)

            # 3. Direct SQL Linkage of Properties to Buildings
            self.env.cr.execute("""
                UPDATE product_product 
                SET building_id = (SELECT id FROM property_building WHERE name = 'Park Station' LIMIT 1),
                    is_property_unit = true
                WHERE id IN (
                    SELECT pp.id FROM product_product pp 
                    JOIN product_template pt ON pp.product_tmpl_id = pt.id 
                    WHERE pt.name ILIKE '%Office%' OR pt.name ILIKE '%Park Station%'
                );

                UPDATE product_product 
                SET building_id = (SELECT id FROM property_building WHERE name = 'Immeuble Bellevue' LIMIT 1),
                    is_property_unit = true
                WHERE id IN (
                    SELECT pp.id FROM product_product pp 
                    JOIN product_template pt ON pp.product_tmpl_id = pt.id 
                    WHERE pt.name ILIKE '%Uccle%' OR pt.name ILIKE '%Bellevue%'
                );

                UPDATE product_product 
                SET building_id = (SELECT id FROM property_building WHERE name = 'Ferme Saint-Jean' LIMIT 1),
                    is_property_unit = true
                WHERE id IN (
                    SELECT pp.id FROM product_product pp 
                    JOIN product_template pt ON pp.product_tmpl_id = pt.id 
                    WHERE pt.name ILIKE '%Apartment%' OR pt.name ILIKE '%Ferme%'
                );
            """)
        except Exception:
            pass
