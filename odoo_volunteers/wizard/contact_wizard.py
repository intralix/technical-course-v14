# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContactWizard(models.TransientModel):
    _name = 'volunteers.contact.wizard'
    _description = 'Wizard: wizard conatct volunteers'

    def _default_contact(self):
        return self.env['cooperative.volunteers'].browse(self._context.get('active_id'))

    task_id = fields.Many2one(comodel_name='cooperative.volunteers',
                                string='task',
                                required=True,
                                default=_default_contact
                                )

    task_volunteer_ids = fields.Many2many(comodel_name='res.partner',
                                            string='Volunteers',
                                            related='task_id.volunteer_ids')

    volunteer_ids = fields.Many2many(comodel_name='res.partner',string='Volunteers_con')

    def create_volunteers(self):
        self.task_id.volunteer_ids |= self.volunteer_ids
        