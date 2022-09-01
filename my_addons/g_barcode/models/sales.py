
from random import choice
from string import digits
from odoo import models


class sales(models.Model):
     _inherit = 'product.template'
     

#@api.multi
def write(self, values):
    if self.barcode:
        for employee in self:
            employee.barcode = '041'+"".join(choice(digits) for i in range(9))
    result = super(sales, self).write(values)
    return result

     
# def generate_random_barcode(self):
#     for employee in self:
#         employee.barcode = '041'+"".join(choice(digits) for i in range(9))