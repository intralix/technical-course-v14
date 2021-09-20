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
    leader = fields.Many2one(
        comodel_name='res.partner',
        string='Leader'
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
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    repeat = fields.Boolean(
        string='Active',
        default=False
    )
    recurrence = fields.Text(
        string='Recurrence'
    )
    volunteer_ids = fields.Many2many(
        comodel_name='res.partner',
        inverse_name='volunteer_id',
        string='Volunteer'
    )
    @api.onchange('leader')
    def _onchange_total_price(self):
        self.state = 'ready'