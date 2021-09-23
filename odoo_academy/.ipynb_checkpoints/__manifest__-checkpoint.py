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
    'version' : '0.0.3',
    'depends' : ['base','sale','website'],

    
    'data' : [
        'security/academy_security.xml',
        'security/ir.model.access.csv',        
        'views/academy_menu_items.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sales_view_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_template.xml',
        'views/academy_web_templates.xml'
        'wizard/sale_wizard_view.xml'
    ],
    
    'demo' : [
        'demo/academy_demo.xml'
    ],
}