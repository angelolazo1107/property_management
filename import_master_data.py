#!/usr/bin/env python3
"""
Odoo XML-RPC Master Data Auto-Importer
This script connects to your Odoo instance and imports all CSV templates automatically.
"""

import csv
import os
import sys
import xmlrpc.client

# --- CONFIGURATION FOR ALON HARAYA UAT ---
ODOO_URL = os.environ.get('ODOO_URL', 'https://alon-haraya-uat.odoo.com')
DB_NAME = os.environ.get('ODOO_DB', 'alon-haraya-uat')
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
    print(f"\nImporting Tenants from {csv_filepath}...")
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
                'is_tenant': True,
                'email': row.get('email', ''),
                'phone': row.get('phone', ''),
                'street': row.get('street', ''),
                'city': row.get('city', ''),
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'search', [[['name', '=', row['name']]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'write', [existing, tenant_data])
                print(f"  [UPDATED] Tenant: {row['name']}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [tenant_data])
                print(f"  [CREATED] Tenant: {row['name']} (ID: {new_id})")


def import_units(uid, models, csv_filepath):
    print(f"\nImporting Units from {csv_filepath}...")
    if not os.path.exists(csv_filepath):
        print(f"  [SKIP] File not found: {csv_filepath}")
        return
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Lookup building ID
            bldg_name = row.get('building_id', row.get('building', ''))
            bldg_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'property.building', 'search', [[['name', '=', bldg_name]]])
            bldg_id = bldg_ids[0] if bldg_ids else False
            if not bldg_id and bldg_name:
                bldg_id = models.execute_kw(DB_NAME, uid, API_KEY, 'property.building', 'create', [{'name': bldg_name}])
                print(f"  [CREATED] Building: {bldg_name} (ID: {bldg_id})")

            unit_name = row.get('name', row.get('unit_name', ''))
            unit_data = {
                'name': unit_name,
                'building_id': bldg_id,
                'floor': row.get('floor', ''),
                'unit_type': row.get('unit_type', 'residential').lower(),
                'area_sqm': float(row.get('area_sqm', 0.0)),
                'monthly_rate': float(row.get('monthly_rate', 0.0)),
                'status': row.get('status', 'available').lower(),
                'electricity_meter_no': row.get('electricity_meter_no', ''),
                'water_meter_no': row.get('water_meter_no', ''),
                'notes': row.get('notes', ''),
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'search', [[['name', '=', unit_name]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'write', [existing, unit_data])
                print(f"  [UPDATED] Unit: {unit_name}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'create', [unit_data])
                print(f"  [CREATED] Unit: {unit_name} (ID: {new_id})")


def import_vendors(uid, models, csv_filepath):
    print(f"\nImporting Vendors from {csv_filepath}...")
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
                'is_vendor': True,
                'email': row.get('email', ''),
                'phone': row.get('phone', ''),
                'vat': row.get('vat', row.get('tin_number', '')),
                'street': row.get('street', ''),
                'city': row.get('city', ''),
                'comment': row.get('comment', row.get('notes', '')),
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'search', [[['name', '=', vendor_name]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'write', [existing, vendor_data])
                print(f"  [UPDATED] Vendor: {vendor_name}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [vendor_data])
                print(f"  [CREATED] Vendor: {vendor_name} (ID: {new_id})")


def import_approval_matrix(uid, models, csv_filepath):
    print(f"\nImporting Approval Matrix from {csv_filepath}...")
    if not os.path.exists(csv_filepath):
        print(f"  [SKIP] File not found: {csv_filepath}")
        return
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            matrix_data = {
                'name': row.get('name', f"{row.get('module')} - {row.get('transaction_type')}"),
                'module': row.get('module', 'Purchase'),
                'transaction_type': row.get('transaction_type', ''),
                'min_amount': float(row.get('min_amount', 0.0)),
                'max_amount': float(row.get('max_amount', 0.0)),
                'required_approvers': row.get('required_approvers', ''),
                'escalation_approver': row.get('escalation_approver', ''),
                'notes': row.get('notes', ''),
            }
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'approval.matrix', 'search', [[['name', '=', matrix_data['name']]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'approval.matrix', 'write', [existing, matrix_data])
                print(f"  [UPDATED] Matrix Rule: {matrix_data['name']}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'approval.matrix', 'create', [matrix_data])
                print(f"  [CREATED] Matrix Rule: {matrix_data['name']} (ID: {new_id})")


def import_utility_readings(uid, models, csv_filepath):
    print(f"\nImporting Utility Readings from {csv_filepath}...")
    if not os.path.exists(csv_filepath):
        print(f"  [SKIP] File not found: {csv_filepath}")
        return
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            unit_name = row.get('unit_id', row.get('unit_name', ''))
            unit_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'search', [[['name', '=', unit_name]]])
            unit_id = unit_ids[0] if unit_ids else False

            tenant_name = row.get('tenant_id', row.get('tenant_name', ''))
            tenant_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'search', [[['name', '=', tenant_name]]])
            tenant_id = tenant_ids[0] if tenant_ids else False

            reading_data = {
                'unit_id': unit_id,
                'tenant_id': tenant_id,
                'reading_date': row.get('reading_date', ''),
                'meter_type': row.get('meter_type', 'electricity').lower(),
                'previous_reading': float(row.get('previous_reading', 0.0)),
                'current_reading': float(row.get('current_reading', 0.0)),
                'rate_per_unit': float(row.get('rate_per_unit', 0.0)),
                'status': row.get('status', 'draft').lower(),
            }
            if unit_id:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'pmo.utility.reading', 'create', [reading_data])
                print(f"  [CREATED] Utility Reading for {unit_name} (ID: {new_id})")
            else:
                print(f"  [WARNING] Unit '{unit_name}' not found. Skipping reading.")


if __name__ == '__main__':
    print("=== Odoo Data Import Utility ===")
    if USERNAME == 'your_admin_email@domain.com':
        print("Notice: Configuration unpopulated. Set ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD env vars to run live import.")
    else:
        uid, models = connect_odoo()
        import_tenants(uid, models, 'templates/tenants_template.csv')
        import_units(uid, models, 'templates/units_template.csv')
        import_vendors(uid, models, 'templates/vendors_template.csv')
        import_approval_matrix(uid, models, 'templates/approval_matrix_template.csv')
        import_utility_readings(uid, models, 'templates/utility_readings_template.csv')
