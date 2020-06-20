# -*- coding: utf-8 -*-
{
    'name': "Open Academy Two",

    'summary': """
        Learning Building A Module""",

    'description': """
        Building a module in odoo12
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/openacademy2.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/wizard.xml',
        'views/report.xml',
        'views/session_board.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}