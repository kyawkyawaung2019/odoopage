from odoo import models, fields, api


class Course(models.Model):
    _name = "open_academy_1.course"
    _description = "Open Academy One Course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
