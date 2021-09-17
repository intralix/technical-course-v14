# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Space(models.Model):
    _name = 'space.space'
    _description = 'Information About spaceShips'
    name = fields.Char(string='Nombre',required=True)
    
    description = fields.Text(string='Descripción de la nave')
    
    width = fields.Integer(string='Anchura (Mts)',required=True)
    height = fields.Integer(string='Altura (Mts)',required=True)
    
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

    base_price = fields.Float(string='Base Price', default=0.00)

    additional_fee = fields.Float(string='Additional Fee',default=0.00)

    total_price = fields.Float(string='Total price',readonly=True)

    @api.onchange('base_price','additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative')

        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional Fees cannot be less than 10.10: %s' % record.additional_fee) 