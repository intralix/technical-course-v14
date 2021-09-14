# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Space(models.Model):
    _name = 'space.space'
    _description = 'Information About spaceShips'

    name = fields.Char(string='Title',required=True)
    
    description = fields.Text(string='Description')
    
    width = fields.Integer(string='Width',required=True)
    height = fields.Integer(string='Height',required=True)
    
    fueltype = fields.Selection(string='fuelType',
                            selection=[
                                ('diesel','Diesel'),
                                ('gas','Gas'),
                                ('volts','Volts')
                                     ],
                             copy=False)
    
    shiptype = fields.Selection(string='shipType',
                            selection=[
                                ('moenix','Moenix'),
                                ('goliath','Goliath'),
                                ('perum','Perum')
                                     ],
                             copy=False)
    
    passengers = fields.Integer(string='Passengers',required=False)
    
    active = fields.Boolean(string='Active')