# -*- coding: utf-8 -*-

{
    'name' : 'Odoo Academy',
    'summary' : 'Academy app to manage Trainig',
    'description' : """Academy Module to manage Training
        - Courses
        - Sessions
        - Attendees
    """,
    'author' : 'Javina',
    'website' : 'https://www.odoo.com',
    'category' : 'training',
    'version' : '0.0.2',
    'depends' : ['base','sale'],
    
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',        
        'views/academy_menu_items.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sales_view_inherit.xml'
    ],
    
    'demo' : [
        'demo/academy_demo.xml'
    ],
}