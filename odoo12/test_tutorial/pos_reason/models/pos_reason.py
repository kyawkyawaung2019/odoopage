from odoo import models, fields


class PosReason(models.Model):
    _name = "pos.reason"
    name = fields.Char(string="Buying Reason")
