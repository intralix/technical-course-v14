# -*- coding: utf-8 -*-

{
    'name' : 'Odoo library',
    'description' : 'Module for management of books',
    'author' : 'logica mobile',
    'website' : 'https://www.intralix.com',
    'version' : '0.0.5',
    'depends' : ['base'],
    'category' : 'training',
    'data' : [            
            'views/books_views.xml',
            'security/library_security.xml',
            'security/ir.model.access.csv',
    ],
    'demo' : [ 
        'demo/library_demo.xml'
        ]   
}