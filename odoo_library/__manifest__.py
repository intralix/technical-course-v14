# -*- coding: utf-8 -*-

{
    'name' : 'Odoo library',
    'description' : 'Module for management of books',
    'author' : 'logica mobile',
    'website' : 'https://www.intralix.com',
    'version' : '0.0.6',
    'depends' : ['base','web_map'],
    'category' : 'training',
    'data' : [            
            
            'security/library_security.xml',
            'security/ir.model.access.csv',
            'views/library_menuitems.xml',
            'views/books_views.xml',
            'views/renting_views.xml'

    ],
    'demo' : [ 
        'demo/library_demo.xml'
        ]   
}