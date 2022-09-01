# -*- coding: utf-8 -*-
{
    'name': " Report Layout",

    'summary': """
      Report Layout for Qweb Pdf reports""",

    'description': """
       This module is used to adjust the layout of the pdf report document
    """,

    'author': "Loyal It Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base','web',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/layout.xml',

        'views/views.xml',
        'views/templates.xml',
        'wizard/base_document_layout_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {

            'web.report_assets_common': [
                'loyal_report_document/static/src/style.css',
                'loyal_report_document/static/src/scss/arialfont.scss',

            ],


        },
}
