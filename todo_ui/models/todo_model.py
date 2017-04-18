# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Tag(models.Model):
    _name = 'todo.taks.tag'
    _description = 'To-Do  Tag'
    name = fields.Char('Name', 40, translate=True)

class Stage(models.Model):
    _name = 'todo.task.stage'
    _description = 'To-do Stage'
    _order = 'sequence,name'
    #string fields
    name = fields.Char('Name', 40 , translate=True)
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
    perc_complete = float.Float(' % Complete', (3, 2))
    # Date fields
    date_effective = fields.Date('Effective Date')
    date_changed = fields.DateTime('Last changed')
    #other fields
    fold = fields.Boolean('Folded?')
    image = fields.Binary('Image')

