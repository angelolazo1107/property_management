# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyDocumentCategory(models.Model):
    _name = 'property.document.category'
    _description = 'Odoo Documents Directory & Folder Tagging'

    name = fields.Char(string='Document Folder / Tag Name', required=True)
    code = fields.Char(string='Folder Code')
    module_scope = fields.Selection([
        ('leasing', 'Leasing Operations'),
        ('pmo', 'PMO Operations'),
        ('procurement', 'Procurement & Canvass'),
        ('accounting', 'Accounting & Billing'),
        ('admin_fleet', 'Admin, Supplies & Fleet'),
    ], string='Module Scope', required=True)
    
    folder_type = fields.Selection([
        ('1_leasing_docs', '1. Leasing Documents'),
        ('2_tenant_docs', '2. Tenant Documents'),
        ('3_lease_contracts', '3. Lease Contracts'),
        ('4_signed_contracts', '4. Signed Contracts'),
        ('5_notarized_contracts', '5. Notarized Contracts'),
        ('6_reservation_payments', '6. Reservation Payments'),
        ('7_move_in_forms', '7. Move-In Forms'),
        ('8_move_out_forms', '8. Move-Out Forms'),
        ('9_pmo_inspections', '9. PMO Inspections'),
        ('10_utility_meter_readings', '10. Utility Meter Readings'),
        ('11_jo_forms', '11. Job Order Forms'),
        ('12_jo_payments', '12. Job Order Payments'),
        ('13_procurement_docs', '13. Procurement Documents'),
        ('14_purchase_reqs', '14. Purchase Requisitions'),
        ('15_canvass_sheets', '15. Canvass Sheets'),
        ('16_supplier_quotes', '16. Supplier Quotations'),
        ('17_purchase_orders', '17. Purchase Orders'),
        ('18_delivery_receipts', '18. Delivery Receipts'),
        ('19_goods_receipts', '19. Goods Receipts'),
        ('20_payment_requests', '20. Payment Requests'),
        ('21_accounting_docs', '21. Accounting Documents'),
        ('22_refund_docs', '22. Refund Documents'),
        ('23_osr_forms', '23. Office Supplies Requests'),
        ('24_vehicle_requests', '24. Vehicle Requests'),
        ('25_vehicle_trip_records', '25. Vehicle Trip Records'),
        ('26_collection_records', '26. Collection Records'),
        ('27_proof_of_payment', '27. Proof of Payment'),
        ('28_ack_receipts', '28. Acknowledgement Receipts'),
    ], string='Folder Designation', required=True)

    parent_id = fields.Many2one('property.document.category', string='Parent Directory')
    is_restricted = fields.Boolean(string='Restricted Document Access', default=False)
    description = fields.Text(string='Compliance & Archival Guidelines')

    @api.model
    def create_tenant_subfolders(self, property_name='Property', unit_name='Unit', tenant_name='Tenant'):
        """
        Creates directory structure: Tenant Files / Property / Unit / Tenant Name
        Subfolders:
        - Valid ID
        - Proof of Income
        - BIS
        - Lease Contract
        - Receipts
        - Access Card / Biometrics
        - Parking
        - Wi-Fi
        - Pet Registration
        - Move-In / Move-Out
        - Refund Documents
        """
        subfolders = [
            'Valid ID',
            'Proof of Income',
            'BIS',
            'Lease Contract',
            'Receipts',
            'Access Card / Biometrics',
            'Parking',
            'Wi-Fi',
            'Pet Registration',
            'Move-In / Move-Out',
            'Refund Documents',
        ]
        
        root_path = f"Tenant Files / {property_name} / {unit_name} / {tenant_name}"
        created_cats = []
        for sf in subfolders:
            folder_name = f"{root_path} / {sf}"
            existing = self.search([('name', '=', folder_name)], limit=1)
            if not existing:
                cat = self.create({
                    'name': folder_name,
                    'code': f"DOC-{sf.upper().replace(' ', '_').replace('/', '_')}",
                    'module_scope': 'leasing',
                    'folder_type': '2_tenant_docs',
                    'description': f"Automated archival folder for {tenant_name} ({unit_name}) - {sf}"
                })
                created_cats.append(cat)
        return created_cats
