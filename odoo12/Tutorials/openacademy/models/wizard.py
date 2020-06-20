from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'open_academy.wizard'
    _description = 'Wizard: Quick registration of attendees to session'

    def _default_sessions(self):
        return self.env['open_academy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2one('res.open_academy_session', string="Session", required=True,
                                  default=_default_sessions)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self:
            session.attendee_ids |= self.attendee_ids
        return {}