# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.addons.base.res.res_request import referenceable_models
from odoo.exceptions import ValidationError

class Tag(models.Model):
    _name = 'todo.task.tag'
    _description = 'To-Do  Tag'
    _parent_store = True
    name = fields.Char('Name', size=40, translate=True)
    tasks_ids = fields.Many2many(
        'todo.task',
        string='Tasks')
    parent_id = fields.Many2one(
        'todo.task.tag',
        'Parent Tag',
        ondelete='restrict')
    parent_left = fields.Integer('Parent Left', index=True)
    parent_right = fields.Integer('Parent Right', index=True)
    child_ids = fields.One2many(
        'todo.task.tag',
        'parent_id',
        'Child Tags')


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
    fold = fields.Boolean( 'Folded?')
    image = fields.Binary('Image')
    #Stage inverse relation O2M
    task_ids = fields.One2many(
        'todo.task',
        'stage_id',
        'Tasks in this stage')


class TodoTask(models.Model):
    _name = 'todo.task'
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')
    refers_to = fields.Reference(referenceable_models,'Refers to')

    stage_fold = fields.Boolean(
        'Stage Folded?',
        compute='_compute_stage_fold',
        search='_search_stage_fold',
        inverse='_write_stage_fold'
    )
    stage_state = fields.Selection(
        related='stage_id.state',
        string='Stage State'
    )

    @api.depends('stage_id.fold')
    def _compute_stage_fold(self):
        for task in self:
            task.stage_fold = task.stage_id.fold

    def _search_stage_fold(self, operator, value):
        return [('stage_id.fold', operator, value)]

    def _write_stage_fold(self):
        self.stage_id.fold = self.stage_fold

    # sql constraint
    _sql_constraints = [
    ('todo_task_name_uniq',
    'UNIQUE (name, active)',
    'Task title must be unique!')]

    @api.constrains('name')
    def _check_name_size(self):
        for todo in self:
            if len(todo.name) < 5:
                raise ValidationError('Must have 5 chars!')
