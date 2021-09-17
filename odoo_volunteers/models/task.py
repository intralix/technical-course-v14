# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class task(models.Model):

    _name = 'cooperative.volunteers'
    _description = 'Volunteers Info'

    name = fields.Char(
        string='Name',
        required=True
    )
    description = fields.Text(
        string='Description'
    )
    leader = fields.Char(
        string='Leader',
        required=True
    )
    state = fields.Selection(string="State",
        selection=[
            ('draft','Draft'),
            ('ready','Ready'),
            ('in progress','In progress'),
            ('finish','Finish')
        ],
        copy=False
    )
    type = fields.Char(
        string='Type',
        required=True
    )
    start_date = fields.Date()
    end_date = fields.Date()
    repeat = fields.Boolean(
        string='Active',
        default=False
    )
    recurrence = fields.Text(
        string='Recurrence'
    )

    @api.onchange('leader')
    def _onchange_total_price(self):
        self.state = 'ready'