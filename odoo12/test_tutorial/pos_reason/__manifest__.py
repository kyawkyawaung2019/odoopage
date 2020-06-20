# -*- coding: utf-8 -*-
{
    'name': "pos_reason",

    'summary': """
        To Choose customer buying reason in POS""",

    'description': """
       To Choose customer buying reason in POS
    """,

    'author': "BEE Data Myanmar",
    'website': "http://www.beedatamyanmar.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/pos_reason_view.xml',
        'views/pos_order.xml',
        'views/pos_templates.xml',
    ],

    'qweb': [
        'static/src/xml/*.xml',
    ],
}