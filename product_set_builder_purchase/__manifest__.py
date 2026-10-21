# -*- coding: utf-8 -*-

{
    'name': 'Product Set Builder - Purchase',
    'category': 'Technical',
    'summary': 'Add product set components to purchase orders',
    'version': '18.0.1.0.0',
    'sequence': 50,
    'author': 'Wai Phyo Oo',
    'website': 'https://www.smartravens.com/',
    'images': ['static/description/cover.png', 'static/description/add_po_3.png'],
    'description': """Extend Product Set Builder to add product set components
        to purchase orders using a quantity-based wizard.
        Requires the product_set_builder addon.
        """,
    'depends': [
        'product_set_builder',
        'purchase',
    ],
    'qweb': [],
    'data': [
        'views/purchase_order_views.xml',
        'wizard/add_product_set_product_views.xml',
    ],
    'price': 0.0,
    'currency': 'USD',
    'support': 'https://www.smartravens.com/',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
