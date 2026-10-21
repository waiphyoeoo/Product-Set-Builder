# -*- coding: utf-8 -*-

{
    'name': 'Product Set Builder - Inventory',
    'category': 'Technical',
    'summary': 'Add product set components to draft stock transfers',
    'version': '18.0.1.0.0',
    'sequence': 50,
    'author': 'Wai Phyo Oo',
    'website': 'https://www.smartravens.com/',
    'images': ['static/description/product_set_components.png'],
    'description': """Extend Product Set Builder to add component stock moves
        to draft inventory transfers through a product set selection wizard.
        Requires the product_set_builder addon.
        """,
    'depends': [
        'product_set_builder',
        'stock',
    ],
    'qweb': [],
    'data': [
        'views/views.xml',
        'wizard/views.xml',
    ],
    'price': 0.0,
    'currency': 'USD',
    'support': 'https://www.smartravens.com/',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
