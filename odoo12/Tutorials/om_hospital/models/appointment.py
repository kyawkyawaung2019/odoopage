from odoo import models, fields, api, _


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = "Appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'appointment_date desc'

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_done(self):
        for rec in self:
            rec.state = 'done'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment.sequence') or _('New')
        result = super(HospitalAppointment, self).create(vals)
        return result

    @api.multi
    def write(self, vals):
        res = super(HospitalAppointment, self).write(vals)
        print("Test write function")
        # To write something here
        return res

    def _get_default_note(self):
        return 2

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, default=_get_default_note)
    patient_age = fields.Integer('Age', related='patient_id.patient_age')
    notes = fields.Text(string="Registration Notes")
    doctor_notes = fields.Text(string="Doctor Notes")
    appointment_lines = fields.One2many('hospital.appointment.line', 'appointment_id', string="Appointment Lines")
    pharmacy_notes = fields.Text(string="Pharmacy Notes")
    appointment_date = fields.Date(string="Date")

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string="Status", indexed=True, readonly=True, default='draft')


