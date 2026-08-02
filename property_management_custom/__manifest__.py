# -*- coding: utf-8 -*-
{
    'name': 'Property Management Extensions for Odoo Apps',
    'version': '19.0.1.0.0',
    'category': 'Customizations',
    'summary': 'Customizations for CRM, Sales, Purchase, Maintenance, Helpdesk, Fleet, Approvals & Accounting',
    'description': """
Property Management Customization Extension for Odoo.sh Installed Apps
======================================================================
Customizes standard Odoo Enterprise apps (CRM, Sales, Purchase, Maintenance, Helpdesk, Fleet, Approvals, Accounting):
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
        'data/crm_stage_data.xml',
        'views/tenant_views.xml',
        'views/property_unit_views.xml',
        'views/crm_lead_views.xml',
        'views/lease_contract_views.xml',
        'views/pmo_inspection_views.xml',
        'views/pmo_views.xml',
        'views/procurement_views.xml',
        'views/fleet_views.xml',
        'views/office_supply_views.xml',
        'views/approval_matrix_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
