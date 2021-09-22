# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectWizard(models.TransientModel):
    _name='space.mission.wizard'
    _description='Asistente: Crear proyecto para la misión'

    def _default_mission(self):
        return self.env['space.mission'].browse(self._context.get('active_id'))

    mission_id = fields.Many2one(comodel_name='space.mission', string='Misión del asistente',required=True,default=_default_mission)

    project_ids =  fields.One2many(comodel_name='project.project',string='Proyectos',inverse_name='mission_id')
    
    def create_mission_project(self):
        return
        #for project in self.project_ids:
        #    project.mission_id = 
