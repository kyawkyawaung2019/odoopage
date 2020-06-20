from odoo import models, fields, api, _


class ResPartners(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartners, self).create(vals_list)
        print("Yes working")
        # do the custom coding here
        return res
