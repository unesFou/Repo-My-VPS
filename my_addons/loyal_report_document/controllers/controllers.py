# -*- coding: utf-8 -*-
# from odoo import http


# class LoyalReportLayout(http.Controller):
#     @http.route('/loyal_report_layout/loyal_report_layout', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/loyal_report_layout/loyal_report_layout/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('loyal_report_layout.listing', {
#             'root': '/loyal_report_layout/loyal_report_layout',
#             'objects': http.request.env['loyal_report_layout.loyal_report_layout'].search([]),
#         })

#     @http.route('/loyal_report_layout/loyal_report_layout/objects/<model("loyal_report_layout.loyal_report_layout"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('loyal_report_layout.object', {
#             'object': obj
#         })
