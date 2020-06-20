from odoo import models, fields, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', string="Gender")
    related_user = fields.Many2one('res.users', ondelete='set null', string="Related User", index=True)
