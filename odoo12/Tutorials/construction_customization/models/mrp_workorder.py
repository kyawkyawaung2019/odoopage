# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_compare, float_round
from odoo.addons import decimal_precision as dp


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    state = fields.Selection([
        ('pending', 'Pending'),
        ('ready', 'Ready'),
        ('progress', 'In Progress'),
        ('qc_test','QC Finished'),
        ('done', 'Finished'),
        ('cancel', 'Cancelled')], string='Status',
        default='pending')

    chemical = fields.Text(string="Chemical")
    temperature = fields.Text(string='Temperature')

    @api.multi
    def button_start(self):
        # res = super(PurchaseOrderLine, self).onchange_product_id()
        res = super(MrpWorkorder, self).button_start()
        self.ensure_one()
        # As button_start is automatically called in the new view
        if self.state in ('done', 'cancel'):
            return True
        return res

    @api.multi
    def button_qc_test(self):
        self.ensure_one()
        # self.end_all()
        return self.write({'state': 'qc_test'})

       