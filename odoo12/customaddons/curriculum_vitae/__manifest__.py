{
    'name': "Curriculum Vitae",
    'author': "White Star",

    'website': "www.whitestart.com.mm",
    'category': "CV From",
    'summary': """
        Odoo ERP Development Tutorial for Myanmar
    """,

    'description': """
        Odoo ERP Development Tutorial for Mynamr
            - To learn the Odoo ERP Development by creating the curriculum_vitae module.
    """,

    'depends': [
        'base_setup',
        'mail',
        'report_xlsx'
    ],

    'data': [
        'security/ir.model.access.csv',

        'views/curriculum_vitae_simple.xml',
        'views/curriculum_vitae_simple_form_view.xml',

        'views/curriculum_vitae.xml',

        'reports/curriculum_vitae_simple_report.xml',
        'reports/curriculum_vitae_simple_excel_report.xml',
    ],
}