# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CopyBook(models.Model):  
    _name = 'library.copybook'
    _description = 'CopyBook'

    _inherits = {
            #'delegation.library': 'library_id',
            'library.book': 'book_id'
        }

    name = fields.Char(string='Name')
    maker = fields.Char(string='Maker')

    """
    # una copia de libro pertenece a una librería
    library_id = fields.Many2one('delegation.library', 
                                  required=True,
                                  ondelete="cascade")
    """
    # una copia de libro pertenece a un libro
    book_id = fields.Many2one('library.book',
                                required=True, 
                                ondelete="cascade")  