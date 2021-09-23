# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Mission(models.Model):
    _name = 'space.mission'
    _description = 'Information About Missions'

    description = fields.Text(string='Descripción de la misión')
    
    space_id = fields.Many2one(comodel_name='space.space',string='Nave Asignada',ondelete='cascade',required=True)

    name = fields.Char(string='Nave espacial',related='space_id.name') 

    tripulation_ids = fields.Many2many(comodel_name='res.partner',string='Tripulantes')

    start_date = fields.Datetime(string='Fecha de lanzamiento')

    end_date = fields.Datetime(string='Fecha de llegada')
    
    active = fields.Boolean(string='Active')

