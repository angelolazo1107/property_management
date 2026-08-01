#!/usr/bin/env python3
"""
Odoo 19.4 XML-RPC Master Data Auto-Importer
This script connects to your Odoo.sh instance and imports the CSV templates automatically.
"""

import csv
import xmlrpc.client
import sys

# --- CONFIGURATION FOR ALON HARAYA UAT ---
ODOO_URL = 'https://alon-haraya-uat.odoo.com'
DB_NAME = 'alon-haraya-uat'  # Or exact DB name on your instance
USERNAME = 'your_admin_email@domain.com'
API_KEY = 'your_api_key_or_password'

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

def import_units(uid, models, csv_filepath):
    print(f"\nImporting Units from {csv_filepath}...")
    with open(csv_filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            unit_data = {
                'name': row['unit_name'],
                'building': row['building'],
                'floor': row['floor'],
                'unit_type': row['unit_type'].lower(),
                'area_sqm': float(row['area_sqm']),
                'monthly_rate': float(row['monthly_rate']),
                'status': row['status'].lower(),
                'electricity_meter_no': row['electricity_meter_no'],
                'water_meter_no': row['water_meter_no'],
                'notes': row['notes'],
            }
            # Search if unit exists
            existing = models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'search', [[['name', '=', row['unit_name']]]])
            if existing:
                models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'write', [existing, unit_data])
                print(f"  [UPDATED] Unit: {row['unit_name']}")
            else:
                new_id = models.execute_kw(DB_NAME, uid, API_KEY, 'property.unit', 'create', [unit_data])
                print(f"  [CREATED] Unit: {row['unit_name']} (ID: {new_id})")

if __name__ == '__main__':
    print("=== Odoo 19.4 Data Import Utility ===")
    # Usage: python import_master_data.py
    # Uncomment lines below after setting credentials:
    # uid, models = connect_odoo()
    # import_units(uid, models, 'templates/units_template.csv')
    print("Configuration ready. Update ODOO_URL and API_KEY to run live import.")
