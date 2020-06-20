from odoo import models, api
import base64
import io


class CurriculumVitaeSimpleExcelReport(models.Model):
    _name = 'report.curriculum_vitae.cv_simple_excel_report_id'
    _inherit = 'report.report_xlsx.abstract'

    @api.multi
    def generate_xlsx_report(self, workbook, data, lines):
        header_format = workbook.add_format({'font_size': 14, 'bold': True, 'align': 'center', 'valign': 'vcenter'})

        sheet = workbook.add_worksheet("Curriculum Vitae Simple")
        sheet.set_column(0, 0, 25)
        sheet.set_column(1, 1, 50)
        sheet.set_column(2, 2, 20)
        sheet.set_row(0, 100)
        sheet.merge_range('A1:B1', 'CURRICULUM VITAE', header_format)

        # cv_image = lines.cv_image
        # image_data = base64.b64decode(cv_image)
        image = io.BytesIO(base64.b64decode(lines.cv_image))
        sheet.insert_image('C1', 'cv_image.png', {'image_data': image, 'x_scale': 0.6, 'y_scale': 0.6})
