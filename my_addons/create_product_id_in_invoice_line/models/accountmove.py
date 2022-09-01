from odoo import api, fields, models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def getAllProduct(self):
        products = self.env['product.product'].search([])
        i=0
        for product in products:
            self.write({'invoice_line_ids':[(0, None, {
                'product_id':product.id,
                'price_unit' : product.list_price,
                'quantity' : product.purchased_product_qty,
                'tax_ids' : product.taxes_id
                
                })]})
            i+=1
            print(i)
            # for vals in vals_list:
            #     move = self.env['account.move'].browse(vals)[0].id
            #     self.env['account.move'].invoice_line_ids.create({
            #         'move_id' : move,
            #         'product_id': product.id,
            #         'price_unit': 2.27
            # })
    #def getAllProduct(self):       
        # products = self.env['product.product'].search([])
        # return {
        #     'type': 'ir.actions.act_window',
        #     'name': "Select Multiples Products",
        #     'view_mode': 'tree',
        #     'res_model': 'product.product',
        #     'target' : 'new'
        # }

   # @classmethod
#     def getAllProduct(self, **kwargs):
#         products = self.env['product.product'].search([])
#         for product in products:
#             return self.env['account.move'].create({
#             'move_type': 'out_invoice',
#             'currency_id': self.env.user.company_id.currency_id,
#             #'partner_id': self.partner_a,
#             'invoice_date': '2021-01-01',
#             'invoice_line_ids': [(0, 0, {
#                 'quantity': 1,
#                 'product_id': product.id,
#                 'price_unit': 100.0,
#                 #'analytic_account_id': analytic_account.id,
#             })]
#         })
# class product(models.Model):
#     _inherit='product.template'
    
#     def select_product(self):
#         return 1

    # def getAllProduct(self):
    #     view = self.env.ref('product.product_template_tree_view')
    #     return {
    #         'name': '采购入库单选择行',
    #         'view_mode': 'form',
    #         'views': [(view.id, 'form')],
    #         'res_model': 'product.template',
    #        # 'res_id': self.ids[0],
    #         'type': 'ir.actions.act_window',
    #         'target': 'new',
    #         # 'domain': [('id', '=', receipt_id)],
    #         # 'context':self.env.context,
    #     }
    
    # def button_select(self):
    #     if self.select == True:
    #         self.select = False
    #     else:
    #         self.select = True
    #     ret = self.order_id.wizard_view()
    #     return ret
    
    