# -*- coding: utf-8 -*-
from odoo import http

# class ClinicCustomization(http.Controller):
#     @http.route('/clinic_customization/clinic_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/clinic_customization/clinic_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('clinic_customization.listing', {
#             'root': '/clinic_customization/clinic_customization',
#             'objects': http.request.env['clinic_customization.clinic_customization'].search([]),
#         })

#     @http.route('/clinic_customization/clinic_customization/objects/<model("clinic_customization.clinic_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('clinic_customization.object', {
#             'object': obj
#         })