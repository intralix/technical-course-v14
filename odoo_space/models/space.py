# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Space(models.Model):
    _name = 'space.space'
    _description = 'Information About spaceShips'
    name = fields.Char(string='Nombre',required=True)
    
    description = fields.Text(string='Descripción de la nave')
    
    width = fields.Integer(string='Anchura',required=True)
    height = fields.Integer(string='Altura',required=True)
    
    fueltype = fields.Selection(string='Consumible',
                            selection=[
                                ('diesel','Diesel'),
                                ('gas','Gas'),
                                ('volts','Volts')
                            ],
                            copy=False)
    
    shiptype = fields.Selection(string='Tipo de nave',
                            selection=[
                                ('moenix','Moenix'),
                                ('goliath','Goliath'),
                                ('perum','Perum')
                            ],
                            copy=False)
    
    passengers = fields.Integer(string='Pasajeros',required=False)
    
    active = fields.Boolean(string='Active')