# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

{
    'name': 'Pharmacy Management Teirab',
    'version': '1.0',
    'sequence': '1',
    'author': 'Acespritech Solutions Pvt. Ltd.',
    'summary': 'POS For Pharmacy',
    'description': "Pharmacy Management Teirab",
    'category': 'Point Of Sale',
    'depends': ['base', 'web', 'point_of_sale','sale',
                'sale_management', 'purchase', 'barcodes',
                'account', 'hr', 'contacts','stock'],
    'price': 1500.00,
    'currency': 'EUR',
    'images': ['static/description/icon.png'],
    
    'assets': {
            'web.assets_backend' : [
                'Pharmacy_Management_Teirab/static/src/css/pos.css',
                'Pharmacy_Management_Teirab/static/src/js/pos.js',
                'Pharmacy_Management_Teirab/static/src/js/test_pos_quantities.js',
                                ]
            },
    'data': [  
        'views/purchase_pharma.xml',
        'views/res_partner.xml',
        'views/views.xml',
        "data.xml",
        'wizard/product_fournisseur_view.xml',
        'views/menu/menu.xml'
        #'security/security_view.xml',
       # 'security/ir.model.access.csv',
    ],
    'qweb': ['static/src/xml/pos.xml'],
   # "qweb": ["static/src/xml/pos.xml"],
   "external_dependencies": {"python": [], "bin": []},

    'installable': True,
    'application': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
