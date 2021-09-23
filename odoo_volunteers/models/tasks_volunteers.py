# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class tasksVolunteers(models.Model):

    _inherit = 'res.partner'
    task_ids = fields.Many2many(
        comodel_name='cooperative.volunteers',
        string='tasks'
    )

