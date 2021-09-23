# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError,ValidationError
import logging
_logger = logging.getLogger(__name__)

class Book(models.Model):    
    _name = 'library.book'
    _description = 'Book of library'
    titulo = fields.Char(string = 'Author',required = True)
    name = fields.Char(string = 'BookName',required = True)
    editores = fields.Char(string = 'Editor',required = True)
    year = fields.Integer(string = 'Year',required = True)   
    isbn = fields.Char(string = 'ISBN',required = True) 
    genre = fields.Char(string = 'Genre',required = True)
    notes = fields.Text(string = 'notes',required = True)


    @api.onchange('isbn')
    def _onchange_length_isbn(self):
        _logger.error("ISBN Value:%s", self.isbn)
        if len(self.isbn) < 13:
            raise UserError('The length of the ISBN cannot be less than 13 characters')