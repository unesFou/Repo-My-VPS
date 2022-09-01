# -*- coding: utf-8 -*-
# from odoo import http


# class ./odoo/myAddons/batcToRef(http.Controller):
#     @http.route('/./odoo/my_addons/batc_to_ref/./odoo/my_addons/batc_to_ref', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/./odoo/my_addons/batc_to_ref/./odoo/my_addons/batc_to_ref/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('./odoo/my_addons/batc_to_ref.listing', {
#             'root': '/./odoo/my_addons/batc_to_ref/./odoo/my_addons/batc_to_ref',
#             'objects': http.request.env['./odoo/my_addons/batc_to_ref../odoo/my_addons/batc_to_ref'].search([]),
#         })

#     @http.route('/./odoo/my_addons/batc_to_ref/./odoo/my_addons/batc_to_ref/objects/<model("./odoo/my_addons/batc_to_ref../odoo/my_addons/batc_to_ref"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('./odoo/my_addons/batc_to_ref.object', {
#             'object': obj
#         })
