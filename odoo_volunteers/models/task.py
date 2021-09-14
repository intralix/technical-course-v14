# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    type = fields.Char(
        string='Type',
        required=True
    )
    date = fields.Date()
    repeat = fields.Boolean(
        string='Active',
        default=False
    )
    recurrence = fields.Text(
        string='Recurrence'
    )