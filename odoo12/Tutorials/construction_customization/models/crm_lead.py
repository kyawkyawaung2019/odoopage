# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Lead(models.Model):
    _inherit = "crm.lead"
    # qc_test= fields.Selection([('pass','Pass'),('fail','Fail')],'Quality Test')
    # check_qc = fields.Boolean('Check QC')

    
    remark=fields.Text('Remark')
    # @api.multi
    # def quality_test(self):
    #     check_qc = False
    #     if self.qc_test == 'pass':
    #         check_qc = True
    #         return self.qc_test
    #     else:
    #         check_qc =True
    #         return "Fail"