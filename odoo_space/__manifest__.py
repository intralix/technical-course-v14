# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space Mission',
    'description': 'Module for go to moon!!',
    'author': 'Intralix BI',
    'website': 'https://www.intralix.com',
    'version': '14.0.1',
    'depends': ['base','contacts','project'],
    'data': [
        'security/space_security.xml',
        'security/ir.model.access.csv',
        'views/space_menuitems.xml',
        'views/space_views.xml',
        'views/mission_views.xml',
        'views/project_views_inherit.xml'
    ],
    'demo': [
        'demo/space_demo.xml',
    ]
}