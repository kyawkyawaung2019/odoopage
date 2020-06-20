from odoo import models, fields


class CurriculumVitae(models.Model):
    _name = 'curriculum.vitae'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name", required=True)
    job_type = fields.Selection([
        ('customer_service', 'Customer Service'),
        ('system_analyser', 'System Analyser'),
        ('software_developer', 'Software Developer'),
        ('web_developer', 'Web Developer'),
        ('quality_assurance', 'Quality Assurance')
    ], string="Job Type", default="software_developer", required=True)
    mobile = fields.Char(string="Mobile")
    email = fields.Char(string="Email")

    age = fields.Integer(string="Age")
    date_of_birth = fields.Datetime(string="Date of Birth")
    nrc = fields.Char(string="NRC")
    nationality = fields.Char(string="Country")
    religion = fields.Char(string="Religion")

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string="Gender", default='male', required=True)
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married')
    ], string="Marital Status", default="single", required=True)
    current_address = fields.Text(string="Current Address")
    objectives = fields.Text(string="Objectives")
