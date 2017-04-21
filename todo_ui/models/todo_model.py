# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Tag(models.Model):
    _name = 'todo.tasks.tag'
    _description = 'To-Do  Tag'
    name = fields.Char('Name', size=40, translate=True)

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'
    #string fields
    name = fields.Char('Name', size=40 , translate=True)
    desc = fields.Text('Description')
    state = fields.Selection(
        [
            ('draft','New'),
            ('open','Started'),
            ('done','Closed'),
        ],
        'State'
    )
    docs = fields.Html('Documentation')
    #Numeric Fields
    sequence = fields.Integer('Sequence')
    perc_complete = fields.Float(' % Complete', (3, 2))
    # Date fields
    date_effective = fields.Date('Effective Date')
    date_changed = fields.Datetime('Last Changed')
    #other fields
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

