# -*- coding: utf-8 -*-
from odoo import http

class SumpurnEntry(http.Controller):
    @http.route('/sumpurn_entry/sumpurn_entry/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/sumpurn_entry/sumpurn_entry/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('sumpurn_entry.listing', {
            'root': '/sumpurn_entry/sumpurn_entry',
            'objects': http.request.env['sumpurn_entry.sumpurn_entry'].search([]),
        })

    @http.route('/sumpurn_entry/sumpurn_entry/objects/<model("sumpurn_entry.sumpurn_entry"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('sumpurn_entry.object', {
            'object': obj
        })