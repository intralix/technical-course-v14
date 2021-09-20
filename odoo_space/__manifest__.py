# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space Mission',
    'description': 'Module for go to moon!!',
    'author': 'Intralix BI',
    'website': 'https://www.intralix.com',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
        'views/space_views.xml',
        'viewsmission_views.xml'
    ],
    'demo': [
        'demo/space_demo.xml',
    ]
}