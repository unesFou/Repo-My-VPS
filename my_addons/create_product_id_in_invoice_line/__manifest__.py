# -*- coding: utf-8 -*-

{
    'name': "Select and create all product_id in invoice_line",
    'version': '1.0',
    'author': 'unesFou',
    'category': 'Base',
    'website': '',
    'license': 'LGPL-3',
    'sequence': 2,
    'price': 0.00,
    'currency': 'USD',
    'summary': """
    App Account Invoice Product Multi Batch Add
    Odoo App of Sunpop.cn
    """,
    'description': """
    
    """,
    'depends': [
        # 'app_web_one2many_multi_add',
        'account',
    ],
    'images': ['static/description/account1.gif'],
    'data': [
        'views/account_move_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'js': [
    ],
    'post_load': None,
    'post_init_hook': None,
    'installable': True,
    'application': True,
    'auto_install': False,
}
