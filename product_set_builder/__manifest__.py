# -*- coding: utf-8 -*-

{
    'name': 'Product Set Builder',
    'category': 'Technical',
    'summary': 'Build product sets, manage components, and filter inventory by set',
    'version': '18.0.1.0.0',
    'sequence': 50,
    'author': 'Wai Phyo Oo',
    'website': 'https://www.smartravens.com/',
    'images': ['static/description/cover.png', 'static/description/product_set_components.png'],
    'description': """Product Set Builder lets you define product sets, manage their component
        quantities, and search or group inventory records by product set.
        Sales and purchase order integration requires compatible extension modules.
        """,
    'depends': [
        'product',
        'stock',
        'account',
        'stock_account'
    ],
    'qweb': [],
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/stock_quant_inherit_views.xml',
        'wizard/add_product_set_product_views.xml',
    ],
    'currency': 'USD',
    'support': 'https://www.smartravens.com/',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
