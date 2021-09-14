# -*- coding: utf-8 -*-

from odoo import models, fields, api

class space(models.Model):
    
    _name = 'space.course'
    _description = 'Space Mission'
    

    name = fields.Char(
        string='Title',
        required=True
    )
    
    description = fields.Text(
        string='Description'
    )
    
    level = fields.Selection(
        string='Level',
        selection=[
            ('junior', 'Junior'),
            ('semi', 'Semi'),
            ('senior', 'Senior'),
        ],
        copy=False
    )
    
    active = fields.Boolean(
        string='Active',
        default=True
    )
