# -*- coding: utf-8 -*-

{
    'name': 'Bundles base module',
    'category': 'Technical',
    'summary': 'Bundles',
    'version': '1.1.1',
    'sequence': 50,
    'author': 'The Fish Consulting',
    'website': 'https://thefishconsulting.be',
    'images': ['static/description/bundle_components.png'],
    'description': """
        
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
        'wizard/add_bundle_product_views.xml',
    ],
    'currency': 'EUR',
    'support': 'contact@thefishconsulting.be',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
