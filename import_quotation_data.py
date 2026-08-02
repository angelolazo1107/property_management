#!/usr/bin/env python3
"""
Odoo XML-RPC Stage 3 Quotation & Reservation Importer & Verification Utility
(Standard Odoo 19 Enterprise Compatible)

This script connects to your Odoo instance via XML-RPC to create/verify:
1. Chart of Accounts line item accounts (Rental Income, Deposit Accounts, etc.)
2. Product Master Data (Monthly Rental, Reservation Fee, Security Deposit, etc.)
3. Quotation Templates (Bare Unit, Furnished Unit, Rental with Parking, Wi-Fi, Access Card, Pet Registration)
"""

import os
import sys
import xmlrpc.client

ODOO_URL = os.environ.get('ODOO_URL', 'https://angelolazo1107-property-management.odoo.sh')
DB_NAME = os.environ.get('ODOO_DB', 'angelolazo1107-property-management-prod')
USERNAME = os.environ.get('ODOO_USER', 'your_admin_email@domain.com')
API_KEY = os.environ.get('ODOO_PASSWORD', 'your_api_key_or_password')

ACCOUNTS_DATA = [
    {'name': 'Rental Income - Property Units', 'code': '400100', 'account_type': 'income'},
    {'name': 'Furniture Rental Income', 'code': '400200', 'account_type': 'income'},
    {'name': 'Parking Fee Income', 'code': '400300', 'account_type': 'income'},
    {'name': 'Internet / Wi-Fi Fee Income', 'code': '400400', 'account_type': 'income'},
    {'name': 'Access Card Fee Income', 'code': '400500', 'account_type': 'income'},
    {'name': 'Pet Registration & Other Lease Income', 'code': '400900', 'account_type': 'income'},
    {'name': 'Unearned Revenue - Reservation Deposits', 'code': '210100', 'account_type': 'liability_current'},
    {'name': 'Security Deposit Payable (Tenant Liabilities)', 'code': '210200', 'account_type': 'liability_current'},
]

PRODUCTS_DATA = [
    {'name': 'Monthly Rental', 'type': 'service', 'list_price': 25000.0, 'account_code': '400100'},
    {'name': 'Furniture Rental Fee', 'type': 'service', 'list_price': 3500.0, 'account_code': '400200'},
    {'name': 'Parking Space Rental Fee', 'type': 'service', 'list_price': 5000.0, 'account_code': '400300'},
    {'name': 'Wi-Fi / Internet Subscription Fee', 'type': 'service', 'list_price': 2000.0, 'account_code': '400400'},
    {'name': 'Building Access Card Fee', 'type': 'service', 'list_price': 500.0, 'account_code': '400500'},
    {'name': 'Pet Registration & Permit Fee', 'type': 'service', 'list_price': 1500.0, 'account_code': '400900'},
    {'name': 'Lease Reservation Deposit Fee', 'type': 'service', 'list_price': 10000.0, 'account_code': '210100'},
    {'name': 'Lease Security Deposit', 'type': 'service', 'list_price': 50000.0, 'account_code': '210200'},
]

TEMPLATES_DATA = [
    {
        'name': 'Bare Unit Rental Quotation Template',
        'products': ['Monthly Rental', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
    {
        'name': 'Furnished Unit Rental Quotation Template',
        'products': ['Monthly Rental', 'Furniture Rental Fee', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
    {
        'name': 'Rental with Parking Quotation Template',
        'products': ['Monthly Rental', 'Parking Space Rental Fee', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
    {
        'name': 'Rental with Wi-Fi Quotation Template',
        'products': ['Monthly Rental', 'Wi-Fi / Internet Subscription Fee', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
    {
        'name': 'Rental with Access Card Quotation Template',
        'products': ['Monthly Rental', 'Building Access Card Fee', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
    {
        'name': 'Rental with Pet Registration Quotation Template',
        'products': ['Monthly Rental', 'Pet Registration & Permit Fee', 'Lease Reservation Deposit Fee', 'Lease Security Deposit']
    },
]

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

def setup_currency(uid, models):
    print("\n--- Setting Up Currency (PHP ₱) ---")
    php_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'res.currency', 'search', [[['name', '=', 'PHP']]])
    if php_ids:
        php_id = php_ids[0]
        models.execute_kw(DB_NAME, uid, API_KEY, 'res.currency', 'write', [[php_id], {'active': True, 'symbol': '₱', 'position': 'before'}])
        company_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'res.company', 'search', [[]])
        if company_ids:
            models.execute_kw(DB_NAME, uid, API_KEY, 'res.company', 'write', [company_ids, {'currency_id': php_id}])
            print(f"  [UPDATED] Main Company Currency set to PHP (₱)")
        pricelist_ids = models.execute_kw(DB_NAME, uid, API_KEY, 'product.pricelist', 'search', [[]])
        if pricelist_ids:
            models.execute_kw(DB_NAME, uid, API_KEY, 'product.pricelist', 'write', [pricelist_ids, {'currency_id': php_id}])
            print(f"  [UPDATED] Public Pricelist Currency set to PHP (₱)")
    else:
        print("  [NOTICE] Currency PHP not found in database registry.")

def setup_accounts(uid, models):
    print("\n--- Setting Up Accounts ---")
    account_map = {}
    for acc in ACCOUNTS_DATA:
        existing = models.execute_kw(DB_NAME, uid, API_KEY, 'account.account', 'search', [[['code', '=', acc['code']]]])
        if existing:
            acc_id = existing[0]
            print(f"  [EXISTS] Account {acc['code']} - {acc['name']}")
        else:
            acc_id = models.execute_kw(DB_NAME, uid, API_KEY, 'account.account', 'create', [acc])
            print(f"  [CREATED] Account {acc['code']} - {acc['name']} (ID: {acc_id})")
        account_map[acc['code']] = acc_id
    return account_map

def setup_products(uid, models, account_map):
    print("\n--- Setting Up Products ---")
    product_map = {}
    for prod in PRODUCTS_DATA:
        acc_id = account_map.get(prod['account_code'])
        vals = {
            'name': prod['name'],
            'type': prod['type'],
            'list_price': prod['list_price'],
            'sale_ok': True,
        }
        if acc_id:
            vals['property_account_income_id'] = acc_id

        existing = models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'search', [[['name', '=', prod['name']]]])
        if existing:
            prod_id = existing[0]
            models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'write', [[prod_id], vals])
            print(f"  [UPDATED] Product {prod['name']} (ID: {prod_id})")
        else:
            prod_id = models.execute_kw(DB_NAME, uid, API_KEY, 'product.product', 'create', [vals])
            print(f"  [CREATED] Product {prod['name']} (ID: {prod_id})")
        product_map[prod['name']] = prod_id
    return product_map

def setup_templates(uid, models, product_map):
    print("\n--- Setting Up Quotation Templates ---")
    for tpl in TEMPLATES_DATA:
        existing = models.execute_kw(DB_NAME, uid, API_KEY, 'sale.order.template', 'search', [[['name', '=', tpl['name']]]])
        line_ids = []
        for p_name in tpl['products']:
            p_id = product_map.get(p_name)
            if p_id:
                line_ids.append((0, 0, {'product_id': p_id, 'product_uom_qty': 1.0}))
        
        tpl_vals = {
            'name': tpl['name'],
            'number_of_days': 30,
            'duration_value': 1,
            'duration_unit': 'year',
            'sale_order_template_line_ids': line_ids
        }
        
        if existing:
            print(f"  [EXISTS] Template: {tpl['name']}")
        else:
            tpl_id = models.execute_kw(DB_NAME, uid, API_KEY, 'sale.order.template', 'create', [tpl_vals])
            print(f"  [CREATED] Template: {tpl['name']} (ID: {tpl_id})")

if __name__ == '__main__':
    print("=== Odoo Stage 3 Quotation & Reservation Master Setup ===")
    if USERNAME == 'your_admin_email@domain.com':
        print("Notice: Configuration unpopulated. Set ODOO_URL, ODOO_DB, ODOO_USER, ODOO_PASSWORD env vars to run live import.")
    else:
        uid, models = connect_odoo()
        setup_currency(uid, models)
        acc_map = setup_accounts(uid, models)
        prod_map = setup_products(uid, models, acc_map)
        setup_templates(uid, models, prod_map)
