# -*- coding: utf-8 -*-

from odoo import http

class Space(http.Controller):
    @http.route('/space/',auth='public',website=True)
    def index(self,**kw):
        return "Hola mundo"

    @http.route('/space/missions/',auth='public',website=True)
    def ships(self,**kw):
        ships = http.request.env['space.space'].search([])
        return http.request.render('odoo_space.space_website',{
            'ships':ships,
        })

    @http.route('/space/<model("space.mission"):mission>/',auth='public',website=True)
    def mission(self,mission):
        return http.request.render('odoo_space.mission_website',{
            'mission':mission,
        })