from odoo import models


class ReportPatientXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'bold': True})
        format2 = workbook.add_format({'font_size': 14, 'align': 'left'})

        sheet = workbook.add_worksheet("Patient Card")

        sheet.write(2, 2, 'Name', format1)
        sheet.write(2, 3, lines.patient_name, format2)

        sheet.write(3, 2, 'Age', format1)
        sheet.write(3, 3, lines.patient_age, format2)

        sheet.write(4, 2, 'Doctor', format1)
        sheet.write(4, 3, lines.name_seq, format2)
