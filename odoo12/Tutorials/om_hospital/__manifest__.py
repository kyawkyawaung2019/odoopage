{
    'name': 'Hospital Management',
    'author': 'Odoo Mates',

    'website': 'odoomates.com',
    'category': 'Extra Tools',
    'summary': 'Module for managing hospital',

    'licence': 'AGPL-3',
    'version': '12.0.0',

    'depends': ['base', 'sale', 'web'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'views/sale_order_inherit.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',

        'data/sequence.xml',
        'data/data.xml',
        'data/mail_template.xml',
        'data/cron.xml',

        'reports/report.xml',
        'reports/patient_card.xml',
        'reports/appointment_card.xml',
        'reports/barcode.xml',

        'wizards/create_appointment.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}