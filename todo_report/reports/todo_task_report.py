# -*- coding: utf-8 -*-
from odoo import models, fields


class TodoReport(models.Model):
    """
    The sql attribute is used to override the database table automatic creation, providing an SQL for that.
    We want it to create a database view to provide the data needed for the report. Our SQL query is quite simple,
    but the point is that we could use any valid SQL query for our view.
    """
    _name = 'todo.task.report'
    _description = 'To-do Report'
    _sql = """
            CREATE OR REPLACE VIEW todo_task_report AS
            SELECT *
            FROM todo_task
            WHERE active = True
        """
    name = fields.Char('Description')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?')
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
