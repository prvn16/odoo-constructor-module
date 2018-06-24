# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sumpurn_entry(models.Model):
    _name = 'sumpurn_entry.sumpurn_entry'
    # fields
    
    TransID1 = fields.Char() # string='TransID1', required='FALSE')
    
    TransDate = fields.Datetime() # string='TransDate', required='FALSE')
    
    TransMode = fields.Char() # string='TransMode', required='FALSE')
    
    Type = fields.Char() # string='Type', required='FALSE')
    
    Comments = fields.Text() # string='Comments', required='FALSE')
    
    Person = fields.Char() # string='Person', required='FALSE')
    
    Invested = fields.Integer() # string='Invested', required='FALSE')
    
    Paid = fields.Integer() # string='Paid', required='FALSE')
    
    Received = fields.Integer() # string='Received', required='FALSE')
    


    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100