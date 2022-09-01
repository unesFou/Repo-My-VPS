from odoo import _ ,api, fields, models

class product_fournisseur(models.Model):
    _name = 'product.fournisseur'
    
    
    def _partner_id(self):
        partner_id = self.env['purchase.order'].search([]).partner_id.ids[0]
        product_ids = self.env['product.template'].search([('seller_ids.name','=',partner_id)])
        return product_ids
   
    product_ids = fields.Many2many('product.product', string="Product" , 
                                    domain="[('purchase_ok','=', True)]", 
                                    default=lambda self: self._partner_id(),
                                    ondelete=None)
                       
 
    def add_product(self):
        for line in self.product_ids:
            self.env['purchase.order.line'].create({
                'product_id': line.id,
                'order_id': self._context.get('active_id')
            })

        
    @api.model
    def create(self,vals):
        return super(product_fournisseur, self).create(vals)
    
    @api.model
    def write(self,vals):
        return super(product_fournisseur, self).write(vals)
    
    @api.model
    def unlink(self,vals):
        return super(product_fournisseur, self).unlink(vals)