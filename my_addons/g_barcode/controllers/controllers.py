# -*- coding: utf-8 -*-
# from odoo import http


# class ./odoo/myAddons/gBarcode(http.Controller):
#     @http.route('/./odoo/my_addons/g_barcode/./odoo/my_addons/g_barcode', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./odoo/my_addons/g_barcode/./odoo/my_addons/g_barcode/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./odoo/my_addons/g_barcode.listing', {
#             'root': '/./odoo/my_addons/g_barcode/./odoo/my_addons/g_barcode',
#             'objects': http.request.env['./odoo/my_addons/g_barcode../odoo/my_addons/g_barcode'].search([]),
#         })

#     @http.route('/./odoo/my_addons/g_barcode/./odoo/my_addons/g_barcode/objects/<model("./odoo/my_addons/g_barcode../odoo/my_addons/g_barcode"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./odoo/my_addons/g_barcode.object', {
#             'object': obj
#         })
