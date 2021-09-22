# -*- coding: utf-8 -*-

{
    'name' : 'Odoo Cooperative Volunteers',
    'description' : 'Cooperative Volunteers',
    'author' : 'Intralix BI',
    'website' : 'https://www.intralix.com',
    'version' : '14.0.3',
    'category' : 'training',
    'depends' : ['base'],
    'data' : [
        'security/volunteers_security.xml',
        'security/ir.model.access.csv',
        'views/volunteers_views.xml',
        'views/approbation_views.xml',
        'views/volunteers_menuitems.xml',
        'wizard/contact_wizard_view.xml'
    ],
    'demo' : [
        'demo/volunteers_demo.xml',
    ]
}