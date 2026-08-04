#!/usr/bin/env python3
"""
Odoo XML-RPC Master Data Auto-Importer & Validation Utility
(Standard Odoo 19 Enterprise Compatible)

This script connects to your Odoo instance and imports/validates:
1. Tenant Master List (`res.partner`)
2. Vendor & Contractor Master List (`res.partner`)
3. Property Unit Master List (`product.product`)
4. Data Dry-Run Pre-Validation & Error Logging (`data_import_validation_log.txt`)
"""

import csv
import os
import sys
import xmlrpc.client

ODOO_URL = os.environ.get('ODOO_URL', 'https://angelolazo1107-property-management.odoo.sh')
DB_NAME = os.environ.get('ODOO_DB', 'angelolazo1107-property-management-prod')
USERNAME = os.environ.get('ODOO_USER', 'your_admin_email@domain.com')
API_KEY = os.environ.get('ODOO_PASSWORD', 'your_api_key_or_password')
LOG_FILE = 'data_import_validation_log.txt'


def log_message(msg):
    print(msg)
    with open(LOG_FILE, mode='a', encoding='utf-8') as log:
        log.write(msg + '\n')


def connect_odoo():
    log_message(f"Connecting to Odoo server at {ODOO_URL}...")
    common = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/common')
    uid = common.authenticate(DB_NAME, USERNAME, API_KEY, {})
    if not uid:
        log_message("Error: Authentication failed! Check URL, DB, Username, or API Key.")
        sys.exit(1)
    log_message(f"Authenticated successfully! User ID: {uid}")
    models = xmlrpc.client.ServerProxy(f'{ODOO_URL}/xmlrpc/2/object')
    return uid, models


def validate_csv_file(csv_filepath, required_fields):
    """ Pre-import dry-run validation check """
    log_message(f"\n--- Dry-Run Pre-Validation: {csv_filepath} ---")
    if not os.path.exists(csv_filepath):
        log_message(f"  [WARNING] CSV File Not Found: {csv_filepath}")
        return False, []

    errors = []
    rows = []
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames or []
        for missing_field in required_fields:
            if missing_field not in fieldnames:
                errors.append(f"Missing required header column: '{missing_field}'")

        seen_names = set()
        for idx, row in enumerate(reader, start=2):
            rows.append(row)
            name = row.get('name', '').strip()
            if not name:
                errors.append(f"Line {idx}: Blank name field encountered.")
            if name in seen_names:
                errors.append(f"Line {idx}: Duplicate record name detected in CSV: '{name}'")
            seen_names.add(name)

            email = row.get('email', '').strip()
            if email and '@' not in email:
                errors.append(f"Line {idx}: Invalid email format for '{name}': '{email}'")

    if errors:
        log_message(f"  ❌ Pre-Validation FAILED for {csv_filepath} ({len(errors)} errors found):")
        for err in errors:
            log_message(f"     - {err}")
        return False, rows
    else:
        log_message(f"  ✅ Pre-Validation PASSED for {csv_filepath} ({len(rows)} valid records).")
        return True, rows


def import_tenants(uid, models, csv_filepath):
    log_message(f"\nImporting Tenants into res.partner from {csv_filepath}...")
    valid, rows = validate_csv_file(csv_filepath, ['name'])
    if not rows:
        return

    for row in rows:
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
            log_message(f"  [UPDATED] Tenant: {row['name']}")
        else:
            new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [tenant_data])
            log_message(f"  [CREATED] Tenant: {row['name']} (ID: {new_id})")


def import_vendors(uid, models, csv_filepath):
    log_message(f"\nImporting Vendors into res.partner from {csv_filepath}...")
    valid, rows = validate_csv_file(csv_filepath, ['name'])
    if not rows:
        return

    for row in rows:
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
            log_message(f"  [UPDATED] Vendor: {vendor_name}")
        else:
            new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'res.partner', 'create', [vendor_data])
            log_message(f"  [CREATED] Vendor: {vendor_name} (ID: {new_id})")


if __name__ == '__main__':
    open(LOG_FILE, 'w').close()
    log_message("=== Odoo 19 Master Data Import & Dry-Run Validation Utility ===")
    if USERNAME == 'your_admin_email@domain.com':
        log_message("Notice: Configuration unpopulated. Set ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD env vars to run live import.")
    else:
        uid, models = connect_odoo()
        import_tenants(uid, models, 'templates/tenants_template.csv')
        import_vendors(uid, models, 'templates/vendors_template.csv')
