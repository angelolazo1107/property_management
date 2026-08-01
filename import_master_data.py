#!/usr/bin/env python3
"""
Odoo XML-RPC Master Data Auto-Importer (Standard Odoo 19 Enterprise Compatible)
This script connects to your Odoo instance and imports all CSV templates automatically.
"""

import csv
import os
import sys
import xmlrpc.client

ODOO_URL = os.environ.get('ODOO_URL', 'https://angelolazo1107-property-management.odoo.sh')
DB_NAME = os.environ.get('ODOO_DB', 'angelolazo1107-property-management-prod')
USERNAME = os.environ.get('ODOO_USER', 'your_admin_email@domain.com')
API_KEY = os.environ.get('ODOO_PASSWORD', 'your_api_key_or_password')


def connect_odoo():
    print(f"Connecting to Odoo server at {ODOO_URL}...")
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(DB_NAME, USERNAME, API_KEY, {})
    if not uid:
        print("Error: Authentication failed! Check URL, DB, Username, or API Key.")
        sys.exit(1)
    print(f"Authenticated successfully! User ID: {uid}")
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models


def import_tenants(uid, models, csv_filepath):
    print(f"\nImporting Tenants into res.partner from {csv_filepath}...")
    if not os.path.exists(csv_filepath):
        print(f"  [SKIP] File not found: {csv_filepath}")
        return
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            is_comp = True if row.get('is_company', '').strip().upper() == 'TRUE' else False
            tenant_data = {
                'name': row['name'],
                'is_company': is_comp,
                'email': row.get('email', ''),
                'phone': row.get('phone', ''),
                'street': row.get('street', ''),
                'city': row.get('city', ''),
                'comment': f"Tenant Account - {row.get('notes', '')}",
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'search', [[['name', '=', row['name']]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'write', [existing, tenant_data])
                print(f"  [UPDATED] Tenant: {row['name']}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [tenant_data])
                print(f"  [CREATED] Tenant: {row['name']} (ID: {new_id})")


def import_vendors(uid, models, csv_filepath):
    print(f"\nImporting Vendors into res.partner from {csv_filepath}...")
    if not os.path.exists(csv_filepath):
        print(f"  [SKIP] File not found: {csv_filepath}")
        return
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            vendor_name = row.get('name', row.get('vendor_name', ''))
            is_comp = True if row.get('is_company', 'TRUE').strip().upper() == 'TRUE' else False
            vendor_data = {
                'name': vendor_name,
                'is_company': is_comp,
                'supplier_rank': 1,
                'email': row.get('email', ''),
                'phone': row.get('phone', ''),
                'vat': row.get('vat', row.get('tin_number', '')),
                'street': row.get('street', ''),
                'city': row.get('city', ''),
                'comment': f"Vendor Account - {row.get('notes', '')}",
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'search', [[['name', '=', vendor_name]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'write', [existing, vendor_data])
                print(f"  [UPDATED] Vendor: {vendor_name}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [vendor_data])
                print(f"  [CREATED] Vendor: {vendor_name} (ID: {new_id})")


if __name__ == '__main__':
    print("=== Odoo 19 Master Data Import Utility ===")
    if USERNAME == 'your_admin_email@domain.com':
        print("Notice: Configuration unpopulated. Set ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD env vars to run live import.")
    else:
        uid, models = connect_odoo()
        import_tenants(uid, models, 'templates/tenants_template.csv')
        import_vendors(uid, models, 'templates/vendors_template.csv')
