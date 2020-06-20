from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    instructor = fields.Boolean('Instructor', default=False)

    session_ids = fields.Many2many('openacademy2.session', string="Attended Session", readonly=True)