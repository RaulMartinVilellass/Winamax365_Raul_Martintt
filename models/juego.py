from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Juego(models.Model):
    _name = "winamax_365.juego"
    _description = "Juego de casino"
    _rec_name = "nombreJuego"
    _order = "nombreJuego"

    nombreJuego = fields.Char(string="Juego", required=True)
    tipoJuego = fields.Selection([('ruleta', 'Ruleta'), ('slot', 'Slot'), ('blackjack', 'Blackjack')], string="Tipo", default='slot', required=True)
    imagenJuego = fields.Binary(string="Imagen / carátula")
    fechaLanzamiento = fields.Date(string="Fecha de lanzamiento", default=fields.Date.context_today)
    rtp = fields.Float(string="RTP (%)", default=96.0)
    activo = fields.Boolean(string="Disponible", default=True)
    numeroFavoritos = fields.Integer(string="Nº de favoritos", compute="_calcular_favoritos", store=True)

    usuario_ids = fields.Many2many("winamax_365.usuario", relation="winamax_usuario_juego_rel", column1="juego_id", column2="usuario_id", string="Jugadores que lo prefieren")

    @api.depends('usuario_ids')
    def _calcular_favoritos(self):
        for j in self:
            j.numeroFavoritos = len(j.usuario_ids)

    @api.constrains('rtp')
    def _comprobar_juego(self):
        for j in self:
            if not 0 <= j.rtp <= 100:
                raise ValidationError("El RTP debe estar entre 0 y 100.")
