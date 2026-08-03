# -*- coding: utf-8 -*-
{
    'name': 'Property Management Extensions for Odoo Apps',
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'summary': 'Customizations for Properties, CRM, Sales, Purchase, Maintenance, Helpdesk, Fleet, Approvals & Accounting',
    'description': """
Property Management Customization Extension for Odoo.sh Installed Apps
======================================================================
Integrates with standard Odoo Enterprise Properties App & core modules:
- Security Visitor Gate Pass custom model with strict validation enforcement.
- Stage 2 Ocular Visit Coordination model linked to CRM Leads & Security GC notifications.
- Extends standard Properties App (product.product) with occupancy status, meter IDs & floor level.
- Extends CRM Lead form with ocular visits, requirements, reservation deposit verification & BIS status.
- Extends Purchase Orders with 3-Supplier Canvass sheets, repeat order controls, and 3-Way Match checkpoints.
- Extends Maintenance & Helpdesk with Move-In/Out inspection checklists, access items, and job orders.
- Extends Fleet with trip consolidation and GSD collection verification.
- Adds unified Approval Matrix rules and Document Management folder structures.
    """,
    'author': 'Coretech Innovations & Solutions Inc.',
    'website': 'https://alon-haraya-uat.odoo.com',
    'depends': [
        'base',
        'crm',
        'calendar',
        'sale_management',
        'account',
        'purchase',
        'stock',
        'maintenance',
        'helpdesk',
        'hr',
        'fleet',
        'website',
        'website_crm',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/currency_data.xml',
        'data/crm_stage_data.xml',
        'data/quotation_account_data.xml',
        'data/quotation_product_data.xml',
        'data/quotation_template_data.xml',
        'data/document_folder_data.xml',
        'data/access_request_sequence.xml',
        'data/wifi_request_sequence.xml',
        'data/parking_application_sequence.xml',
        'data/move_in_form_sequence.xml',
        'data/agent_commission_sequence.xml',
        'data/rental_registration_sequence.xml',
        'data/monthly_billing_sequence.xml',
        'data/billing_cron_data.xml',
        'data/lease_expiration_cron_data.xml',
        'data/move_out_clearance_sequence.xml',
        'data/deposit_refund_sequence.xml',
        'views/tenant_views.xml',
        'views/ocular_visit_views.xml',
        'views/visitor_gate_pass_views.xml',
        'views/crm_lead_views.xml',
        'views/sale_order_views.xml',
        'views/lease_contract_views.xml',
        'views/pmo_inspection_views.xml',
        'views/pmo_views.xml',
        'views/procurement_views.xml',
        'views/fleet_views.xml',
        'views/office_supply_views.xml',
        'views/approval_matrix_views.xml',
        'views/property_reservation_views.xml',
        'views/tenant_application_bis_views.xml',
        'views/unit_assessment_task_views.xml',
        'views/access_request_views.xml',
        'views/wifi_request_views.xml',
        'views/parking_application_views.xml',
        'views/move_in_form_views.xml',
        'views/agent_commission_views.xml',
        'views/rental_registration_views.xml',
        'views/monthly_billing_views.xml',
        'views/move_out_clearance_views.xml',
        'views/deposit_refund_views.xml',
        'views/property_unit_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
