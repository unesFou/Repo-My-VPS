from odoo import _, api,fields, models

class Inheritrespartner(models.Model):
    
    _inherit = "res.partner"
    
    name = fields.Char(string ="name", store=True)
    vat = fields.Char(string ="vat", store=True)
    cr = fields.Char(string="cr", store=True)