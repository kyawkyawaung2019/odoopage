{
    'name': "Curriculum Vitae",
    'author': "White Star",

    'website': "http://www.whitestarmm.com",
    'category': 'CV Form',
    'summary': """
        Odoo ERP Development Tutorial for Myanmar
    """,
    'description': """
        Odoo ERP Development Tutorial for Myanmar
            - To learn the Odoo ERP Development module structure by creating the curriculum vitae.
    """,

    'depends': ['base', 'mail', 'report_xlsx'],

    'data': [
        'security/ir.model.access.csv',
        'views/curriculum_vitae_simple.xml',
        'views/curriculum_vitae_simple_form_view.xml',

        'views/curriculum_vitae.xml',

        'reports/curriculum_vitae_simple_report.xml',
        'reports/curriculum_vitae_simple_excel_report.xml',
    ],
}