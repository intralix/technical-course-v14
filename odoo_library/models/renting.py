# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Renting(models.Model):    
    _name = 'library.renting'
    _description = 'Renting of book info'
    nameclient = fields.Char(string = 'Client Name')
    startdate = fields.Datetime(string = 'Start Date of rent')
    enddate = fields.Datetime(string = 'End Date of rent')
    phone = fields.Char(string = 'Phone Client')

    client_id = fields.Many2one(comodel_name='res.partner',string = 'Client')
    #book_id = fields.Many2many(comodel_name='library.book',string = 'BooksRenting')   
    book_id = fields.Many2many(comodel_name='library.copybook',string = 'BooksCopys')