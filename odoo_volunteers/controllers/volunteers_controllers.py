from odoo import http

class Academy(http.Controller):
    @http.route('/volunteer/',auth='public',website=True)
    def index(self, **kw):
        return "Hello, world"

    @http.route('/volunteer/volunteers/',auth='public', website=True)
    def volunteers(self, **kw):
        volunteers = http.request.env['res.partner'].search([])
        return http.request.render('odoo_volunteers.volunteers_website',{
            'volunteers':volunteers,
        })

    @http.route('/volunteer/<model("cooperative.volunteers"):task>/',auth='public', website=True)
    def task(self, task):
        return http.request.render('odoo_volunteers.task_website',{
            'task':task,
        })