# -*- coding: utf-8 -*-
from odoo import http

class Todo(http.Controller):
    @http.route('/hellocms/<page>', auth='public')
    def hello(self, page, **kwargs):
        return http.request.render(page)

