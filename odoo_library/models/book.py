# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book of library'
    titulo = fields.Char(string = 'Author',required = True)
    name = fields.Char(string = 'BookName',required = True)
    editores = fields.Char(string = 'Editor',required = True)
    year = fields.Integer(string = 'Year',required = True)   
    isbn = fields.Char(string = 'ISBN',required = True) 
    genre = fields.Char(string = 'Genre',Required = True)
