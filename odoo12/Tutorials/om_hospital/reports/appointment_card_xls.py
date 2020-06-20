from odoo import models


class ReportAppointmentXLS(models.AbstractModel):
    _name = 'report.om_hospital.report_appointment_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size': 14, 'bold': True})
        format2 = workbook.add_format({'font_size': 14, 'align': 'left'})

        sheet = workbook.add_worksheet("Appointment Card")

        sheet.write(2, 2, 'Patient Name', format1)
        sheet.write(2, 3, 'Name', format2)

        sheet.write(3, 2, 'Patient Age', format1)
        sheet.write(3, 3, lines.patient_age, format2)

        sheet.write(4, 2, 'Appointment Date', format1)
        sheet.write(4, 3, lines.appointment_date, format2)
