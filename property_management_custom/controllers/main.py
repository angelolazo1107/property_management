# -*- coding: utf-8 -*-
from odoo import http, _
from odoo.http import request
from datetime import datetime

class PropertyManagementWebsiteController(http.Controller):

    @http.route(['/properties', '/properties/page/<int:page>'], type='http', auth='public', website=True)
    def property_catalog(self, occupancy_status=None, **kw):
        domain = [('is_property_unit', '=', True)]
        if occupancy_status:
            domain.append(('occupancy_status', '=', occupancy_status))
        
        units = request.env['product.product'].sudo().search(domain, order='name asc')
        values = {
            'units': units,
            'selected_occupancy': occupancy_status or '',
        }
        return request.render('property_management_custom.property_catalog_template', values)

    @http.route(['/property/inquiry'], type='http', auth='public', website=True)
    def property_inquiry_form(self, unit_id=None, **kw):
        units = request.env['product.product'].sudo().search([('is_property_unit', '=', True)], order='name asc')
        selected_unit = False
        if unit_id:
            selected_unit = request.env['product.product'].sudo().browse(int(unit_id))
            
        values = {
            'units': units,
            'selected_unit': selected_unit,
        }
        return request.render('property_management_custom.property_inquiry_form_template', values)

    @http.route(['/property/inquiry/submit'], type='http', auth='public', methods=['POST'], website=True, csrf=True)
    def property_inquiry_submit(self, **post):
        contact_name = post.get('contact_name')
        email_from = post.get('email_from')
        phone = post.get('phone')
        unit_id = int(post.get('unit_id')) if post.get('unit_id') else False
        intended_move_in_date = post.get('intended_move_in_date') or False
        preferred_budget = float(post.get('preferred_budget')) if post.get('preferred_budget') else 0.0
        parking_required = True if post.get('parking_required') == 'on' else False
        wifi_required = True if post.get('wifi_required') == 'on' else False
        pet_details = post.get('pet_details') or ''
        notes = post.get('notes') or ''

        ocular_date_str = post.get('ocular_visit_date') or False
        
        # 1. Search or Create Partner
        partner = request.env['res.partner'].sudo().search([('email', '=', email_from)], limit=1)
        if not partner and email_from:
            partner = request.env['res.partner'].sudo().create({
                'name': contact_name,
                'email': email_from,
                'phone': phone,
                'is_company': False,
            })

        # 2. Create CRM Lead
        unit_name = 'General'
        if unit_id:
            unit_rec = request.env['product.product'].sudo().browse(unit_id)
            if unit_rec:
                unit_name = unit_rec.name

        lead_vals = {
            'name': f"Website Inquiry: {contact_name} - Unit: {unit_name}",
            'contact_name': contact_name,
            'partner_id': partner.id if partner else False,
            'email_from': email_from,
            'phone': phone,
            'target_unit_id': unit_id,
            'intended_move_in_date': intended_move_in_date,
            'preferred_budget': preferred_budget,
            'parking_required': parking_required,
            'wifi_required': wifi_required,
            'pet_details': pet_details,
            'description': notes,
            'type': 'opportunity',
        }
        
        lead = request.env['crm.lead'].sudo().create(lead_vals)

        # 3. Schedule Ocular Visit if requested
        if ocular_date_str:
            try:
                ocular_datetime = datetime.strptime(ocular_date_str, '%Y-%m-%dT%H:%M')
                request.env['ocular.visit'].sudo().create({
                    'lead_id': lead.id,
                    'visitor_name': contact_name,
                    'contact_number': phone,
                    'unit_id': unit_id,
                    'visit_schedule': ocular_datetime,
                    'security_gate_notified': True,
                    'status': 'scheduled',
                })
                lead.sudo().write({
                    'ocular_status': 'scheduled',
                    'ocular_visit_date': ocular_datetime,
                })
            except Exception:
                pass

        return request.redirect('/property/inquiry/thankyou?lead_id=%s' % lead.id)

    @http.route(['/property/inquiry/thankyou'], type='http', auth='public', website=True)
    def property_inquiry_thankyou(self, lead_id=None, **kw):
        lead = False
        if lead_id:
            lead = request.env['crm.lead'].sudo().browse(int(lead_id))
        return request.render('property_management_custom.property_inquiry_thankyou_template', {'lead': lead})
