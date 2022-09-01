{
    'name': "POS Lot Selection",
    'summary': """POS Lot Selection""",
    'description': """POS Lot Selection""",
    'author': "Meghsundar Private Limited",
    'website': "",
    'category': 'Point of Sale',
    'version': '15.0.1',
    'license': 'AGPL-3',
    'depends': ['web', 'point_of_sale'],
    'data': [
        'views/assets.xml'
    ],
    'assets': {
         'web.assets_backend': [
            'mpl_pos_multi_lot/static/src/**/*',
    ],
        'web.assets_common': [
            'mpl_pos_multi_lot/static/src/js/order_widget.js',
            'mpl_pos_multi_lot/static/src/js/product_lot_popup.js',
            'mpl_pos_multi_lot/static/src/js/product_lot.js',
            'mpl_pos_multi_lot/static/src/js/product_screen.js',
        ],
    },
    'qweb': [
        'static/src/xml/product_lot_popup.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
