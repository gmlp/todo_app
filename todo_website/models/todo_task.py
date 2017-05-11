# -*- coding: utf-8 -*-
from odoo import api, models
from odoo.exceptions import ValidationError, Warning

class TodoTask(models.Model):
    _inherit = 'todo.task'

    @api.model
    def website_form_input_filter(self, request, values):
        import pdb;pdb.set_trace()
        if 'name' in values:
            values['name'] = values['name'].strip()
            if len(values['name']) < 3:
                raise Warning(
                    'Text must be at least 3 characters long'
                )
        return values
