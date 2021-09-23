# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
class approbation(models.Model):

    _name = 'approbation.volunteers'
    _description = 'Items'

    name_item = fields.Char(
        string='Name',
        required=True
    )
class approbationToTask(models.Model):

    _inherit = 'cooperative.volunteers'
    approbation_id = fields.Many2one(
        comodel_name='approbation.volunteers',
        string='approbation'
    )

