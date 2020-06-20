# -*- coding: utf-8 -*-
from odoo import http

# class OpenAcademy1(http.Controller):
#     @http.route('/open_academy_1/open_academy_1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/open_academy_1/open_academy_1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('open_academy_1.listing', {
#             'root': '/open_academy_1/open_academy_1',
#             'objects': http.request.env['open_academy_1.open_academy_1'].search([]),
#         })

#     @http.route('/open_academy_1/open_academy_1/objects/<model("open_academy_1.open_academy_1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('open_academy_1.object', {
#             'object': obj
#         })