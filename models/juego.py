from odoo import models, fields


class Juego(models.Model):
    _name = "winamax_365.juego"
    _description = "Clase de juego de casino"

    nombreJuego = fields.Char(string="Juego", required=True,
                              help="Ej.: Lightning Roulette, Sugar Rush")
    tipoJuego = fields.Selection([
        ('ruleta', 'Ruleta'),
        ('slot', 'Slot'),
    ], string="Tipo", default='slot')
    multiplicadorMaximo = fields.Integer(string="Multiplicador máximo (x)",
                                         help="Multiplicador máximo del juego")
    tieneBonus = fields.Boolean(string="Bonus / giros gratis", default=False)
    tieneJackpot = fields.Boolean(string="Jackpot", default=False)
