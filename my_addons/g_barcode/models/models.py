# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class ./odoo/my_addons/g_barcode(models.Model):
#     _name = './odoo/my_addons/g_barcode../odoo/my_addons/g_barcode'
#     _description = './odoo/my_addons/g_barcode../odoo/my_addons/g_barcode'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
