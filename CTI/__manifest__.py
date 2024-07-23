{
    'name': 'Cloud CTI Integration',
    'version': '8.0',
    'summary': 'Integrate Cloud CTI with Odoo CRM',
    'author': 'Santhiya',
    'category': 'CRM',
    'depends': ['crm'],
    'data': [
        'views/cloud_cti_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'cloud_cti/static/src/js/cloud_cti.js',
        ],
    },
    'installable': True,
    'application': True,
}

    