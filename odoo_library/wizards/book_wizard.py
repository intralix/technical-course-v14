# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookWizard(models.TransientModel):
    _name = 'library.book.wizard'
    _description = 'Wizard: Quick visualization book'

    def _default_session(self):
        return self.env['library.book'].browse(self._context.get('active_id'))

    book_id = fields.Many2one(comodel_name='library.book',
                             string = 'Book',
                             required = True,
                             default = _default_session
                              )
    