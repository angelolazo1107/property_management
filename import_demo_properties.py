#!/usr/bin/env python3
"""
Odoo XML-RPC Demo Property Units Importer Script
(Standard Odoo 19 Enterprise Compatible)

This script imports demo property units from `templates/demo_properties_template.csv`
directly into Odoo `product.product` with `is_property_unit = True`.
"""

import csv
import os
import sys
import xmlrpc.client

ODOO_URL = os.environ.get('ODOO_URL', 'https://angelolazo1107-property-management.odoo.sh')
DB_NAME = os.environ.get('ODOO_DB', 'angelolazo1107-property-management-prod')
USERNAME = os.environ.get('ODOO_USER', 'your_admin_email@domain.com')
API_KEY = os.environ.get('ODOO_PASSWORD', 'your_api_key_or_password')
CSV_FILE = 'templates/demo_properties_template.csv'


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


def import_demo_properties(uid, models):
    print(f"\n--- Importing Demo Property Units from {CSV_FILE} ---")
    if not os.path.exists(CSV_FILE):
        print(f"Error: File not found: {CSV_FILE}")
        return

    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        created_count = 0
        updated_count = 0

        for row in reader:
            unit_name = row['name'].strip()
            property_type = row.get('property_type', 'residential_studio').strip()
            occupancy_status = row.get('occupancy_status', 'available').strip()
            floor_level = row.get('floor_level', '').strip()
            area_sqm = float(row.get('area_sqm', 0.0))
            list_price = float(row.get('list_price', 0.0))
            property_address = row.get('property_address', '').strip()
            electricity_meter_no = row.get('electricity_meter_no', '').strip()
            water_meter_no = row.get('water_meter_no', '').strip()
            description = row.get('description', row.get('notes', '')).strip()

            vals = {
                'name': unit_name,
                'is_property_unit': True,
                'website_published': True,
                'type': 'service',
                'sale_ok': True,
                'purchase_ok': False,
                'property_type': property_type,
                'occupancy_status': occupancy_status,
                'floor_level': floor_level,
                'area_sqm': area_sqm,
                'list_price': list_price,
                'property_address': property_address,
                'electricity_meter_no': electricity_meter_no,
                'water_meter_no': water_meter_no,
                'description': description,
            }

            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'search', [[['name', '=', unit_name]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'write', [existing, vals])
                print(f"  [UPDATED] Property Unit: {unit_name} (Type: {property_type}, Status: {occupancy_status})")
                updated_count += 1
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'create', [vals])
                print(f"  [CREATED] Property Unit: {unit_name} (ID: {new_id}, Type: {property_type}, Status: {occupancy_status})")
                created_count += 1

    print(f"\n✅ Import Complete! Created: {created_count}, Updated: {updated_count}")


if __name__ == '__main__':
    print("=== Odoo 19 Demo Property Units Auto-Importer ===")
    if USERNAME == 'your_admin_email@domain.com':
        print("Notice: Configuration unpopulated. Set ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD env vars to run live import.")
        print(f"CSV Demo Template created at: {CSV_FILE}")
        print("You can also import this CSV file directly via Odoo Web UI (Sales > Products > Favorites > Import Records).")
    else:
        uid, models = connect_odoo()
        import_demo_properties(uid, models)
