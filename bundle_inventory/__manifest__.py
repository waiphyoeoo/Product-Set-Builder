# -*- coding: utf-8 -*-

{
    'name': 'Bundles purchase module',
    'category': 'Technical',
    'summary': 'Bundles',
    'version': '1.1',
    'sequence': 50,
    'author': 'The Green IT',
    'website': 'https://thefishconsulting.be',
    'images': ['static/description/add_po_3.png'],
    'description': """

        """,
    'depends': [
        'bundle',
        'stock',
    ],
    'qweb': [],
    'data': [
        'views/views.xml',
        'wizard/views.xml',
    ],
    'price': 0.0,
    'currency': 'EUR',
    'support': 'contact@thefishconsulting.be',
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
}
