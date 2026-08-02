# -*- coding: utf-8 -*-
{
    'name': 'Property Management Enterprise Core',
    'version': '19.0.1.0.0',
    'category': 'Real Estate / Property Management',
    'summary': 'Centralized Leasing, PMO Operations, Utility Readings, Job Orders, Fleet & Financial Approvals',
    'description': """
Property Management Operating Platform for Odoo 19.0 on Odoo.sh
==============================================================
Centralizes tenant lifecycle, PMO inspections, utility readings, procurement approvals,
fleet trip tracking, and financial verification control gates.
    """,
    'author': 'Coretech Innovations & Solutions Inc.',
    'website': 'https://alon-haraya-uat.odoo.com',
    'depends': [
        'base',
        'crm',
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
        'views/pmo_views.xml',
        'views/procurement_views.xml',
        'views/fleet_views.xml',
        'views/office_supply_views.xml',
        'views/approval_matrix_views.xml',
        'views/menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
