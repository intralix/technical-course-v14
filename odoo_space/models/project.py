# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.One2many(comodel_name='space.mission', string='Misiones de un proyecto',ondelete='set null')
