# -*- coding: utf-8 -*-
from math import prod
from odoo import models, fields


class ProductTemplateBatchToRef(models.Model):
    _inherit = 'product.template'
    
    # Transfert product tracking to Lot
    def transfertToLot(self):
        products = self.env['product.template'].search([])
        for product in products :
            if product.tracking == 'none':
                product.tracking = 'lot'
                print('---------------------------',product.tracking)
                
    #Transfert all product to POS available
    def transfert_to_pos(self):
        products = self.env['product.template'].search([])
        for product in products :
            if product.available_in_pos == False:
                product.available_in_pos = True
                print('---------------------------',(product.available_in_pos == True).bit_length)
    
                
    # Transfert detailed type to product stockable        
    def transfertTostockable(self):
        products = self.env['product.template'].sudo().search([])
        for product in products :
            if product.detailed_type != 'product':
                product.detailed_type = 'product'
                print('---------------------------',product.detailed_type)
            else:
                continue
        
    # Create Ref of product if not existe  
    def transfertToRef(self):
        products = self.env['product.product'].search([])
        products_tmpls = self.env['product.template'].search([])
        #lots = self.env['stock.production.lot'].search([])
        for product in products :
            for product_tmpl in products_tmpls:
                if product_tmpl.id == product.id :
                    if product_tmpl.name :
                        if product_tmpl.batch:
                            #if self.env['stock.production.lot'].product_id.id == product_tmpl.id  :
                                self.env['stock.production.lot'].create({
                                    'name': product_tmpl.batch,
                                    'product_id': product_tmpl.id,
                                    'company_id': self.env.company.id
                                    })
                            # elif self.env['stock.production.lot'].id :
                            #     if self.env['stock.production.lot'].name != product_tmpl.batch :
                            #           #  self.env['stock.production.lot'].name.unlink()
                            #             self.env['stock.production.lot'].write({
                            #             'name': product_tmpl.batch,
                            #             'product_id': product_tmpl.id,
                            #             'company_id': self.env.company.id
                            #             })
                            #     else :
                            #         continue
                    else:
                        continue
                else:
                    continue