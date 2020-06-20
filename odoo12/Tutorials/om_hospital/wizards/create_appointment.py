from odoo import models, fields, api


class CreateAppointment(models.Model):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string="Patient")
    appointment_date = fields.Date(string="Appointment Date")

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'appointment_date': self.appointment_date,
            'notes': "Create from the wizard code"
        }
        self.patient_id.message_post(body="Appointment creation successfully!", subject="Appointment creation")
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("Get data function")
        appointments = self.env['hospital.appointment'].search([])
        for rec in appointments:
            print("Appointment name : ", rec.name)
