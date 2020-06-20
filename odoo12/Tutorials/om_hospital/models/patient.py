from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Record"
    _rec_name = 'patient_name'

    patient_name = fields.Char(string="Name", required=True, track_visibility='always')
    name_seq = fields.Char(string="Patient ID", required=True, copy=False, readonly=True,
                           index=True, default=lambda self: _('New'))
    patient_age = fields.Integer('Age', track_visibility='always')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], default='male', string="Gender")

    patient_name_upper = fields.Char(string="Patient Name Upper", compute='_compute_upper_name',
                                     inverse='_inverse_upper_name')

    @api.model
    def test_cron_job(self):
        print("Abcd")

    @api.depends('patient_name')
    def _compute_upper_name(self):
        for rec in self:
            rec.patient_name_upper = self.patient_name.upper() if rec.patient_name else False

    def _inverse_upper_name(self):
        for rec in self:
            rec.patient_name = self.patient_name_upper.lower() if rec.patient_name_upper else False

    @api.multi
    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s - %s' % (rec.name_seq, rec.patient_name)))
        return res

    @api.constrains('patient_age')
    def check_age(self):
        for rec in self:
            if rec.patient_age <= 5:
                raise ValidationError(_("The age must be greater than 5."))

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age:
                if rec.patient_age < 18:
                    rec.age_group = 'minor'
                else:
                    rec.age_group = 'major'

    @api.multi
    def open_patient_appointment(self):
        return{
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'view_id': False,
        }

    def get_appointment_count(self):
        count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])
        self.appointment_count = count

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for rec in self:
            if rec.doctor_id:
                self.doctor_gender = rec.doctor_id.gender

    age_group = fields.Selection([
        ('minor', 'Minor'),
        ('major', 'Major'),
    ], string="Age Group", compute='set_age_group')
    notes = fields.Text(string="Registration Notes")
    name = fields.Char(string="Contact Number")
    image = fields.Binary(string="Image")
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')
    active = fields.Boolean('Active', default="True")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    doctor_gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Doctor Gender")
    user_id = fields.Many2one('res.users', ondelete='set null', string="PRO", index=True)
    email_id = fields.Char(string="Email", default='admin@example.com')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals)
        return result

    def action_send_card(self):
        template_id = self.env.ref("om_hospital.patient_card_email_template").id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)
