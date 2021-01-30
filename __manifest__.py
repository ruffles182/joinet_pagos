# -*- coding: utf-8 -*-
{
    'name': "Pedidos Joinet",

    'summary': """
        Sistema de administraciòn de pedidos para Joinet""",

    'description': """
        Sistema de administraciòn de pedidos para Joinet
    """,

    'author': "Salvador Arreola",
    'website': "http://www.github.com/Ruffles182",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    'aplication': True,

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
