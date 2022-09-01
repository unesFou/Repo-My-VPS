
from itertools import product
from string import digits
from odoo import _, api,fields, models
from random import choice
from datetime import date
#from string import digits

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    batch = fields.Char(string='Batch')
    eXP = fields.Date(string='EXP')
    w_S_P = fields.Char(string='W.S.P')
    w_R_P = fields.Char(string='W.R.P')
    
    def action_server_expired_date(self):
        print('ttttttttttttttttttttt')    
        return {
                "name" : 'Expired Product',
                "type":"ir.actions.act_window",
                "res_model":"product.template",
                "view_mode":"tree",
                "domain": [('eXP', '<', date.today())]
                #"target":"new"
            }

    
    def g_barcode(self):
        print('barcode')
        if not self.barcode:
            print('barcode',self.barcode)
            for b in self:
                b.barcode = '041'+"".join(choice(digits) for i in range(9))
        

class PurchaseInheritOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    
    qty_available = fields.Char(string='Qty available', readonly=True)
    
    @api.onchange('product_id')
    def get_qty (self):
        self.qty_available = self.product_id.qty_available 
    
class PurchaseOrderInherit(models.Model):
    _inherit = "purchase.order"
    
    name_good = fields.Char('Good')
    
    def getProductsFornisor(self):
        return {
                "name" : self.partner_id.name,
                "type":"ir.actions.act_window",
                "res_model":"product.fournisseur",
                "view_mode":"form",
                "target":"new"
            }
    
       
    @api.onchange('partner_id')
    def onchange_journal_id(self):
        self.partner_ref = self.partner_id.ref    
    