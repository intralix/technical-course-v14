# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.Many2one(comodel_name='space.mission', string='Misión del proyecto',inverse_name='project_ids')

