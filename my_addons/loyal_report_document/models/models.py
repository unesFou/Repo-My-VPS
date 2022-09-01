# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Company(models.Model):

    _inherit = "res.company"

    header_image = fields.Binary(string="Header Image")
    footer_image = fields.Binary(string="Footer Image")
    water_mark = fields.Binary(string="Water Mark")
    company_watermark = fields.Binary(string="Letter Head")
    image_type = fields.Selection([('single_image', 'Single Image'), ('multiple_image', 'Multiple Image')], string="Image Type", required=True)
