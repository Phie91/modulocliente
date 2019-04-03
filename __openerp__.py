# -*- coding: utf-8 -*-

######################################################################

# __openerp__.py

{
    'name': 'Modulo Clientes',
    'version': '1.0',
    'author': 'Stephanie Romero y Eva Leticia Aguilar',
    'category': 'Compra Ventas',
    'summary': 'Modulo de gestions de clientes 2019',
    'sequence': 30,
    'description': """
    """,
    'license' : 'AGPL-3',
    'depends': ['sale','base_setup', 'product', 'analytic', 'report'],
    'data': [
        
        'views/cliente_view.xml',
        
    ],
    'installable': True,
    'active': False,
    'auto_install': False,
}