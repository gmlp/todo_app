from odoo import models, fields
class TodoTask(models.Model):
    _inherit = 'todo.task'
    color = fields.Integer('Color Index')
    priority = fields.Selection(
        [('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High')],
        'Priority', default='1')
    kanban_state = fields.Selection(
        [('normal', 'In Progress'),
        ('done', 'Ready for next stage'),
        ('blocked', 'Blocked')],
        'Kanban State', default='normal')

