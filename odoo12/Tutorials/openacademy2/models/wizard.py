from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'openacademy2.wizard'
    _description = "Wizard: Quick registration of attendee to session"

    def _default_sessions(self):
        return self.env['openacademy2.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2one('openacademy2.session', string="Session", required=True, default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
