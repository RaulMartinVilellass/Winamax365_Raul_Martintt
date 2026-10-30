from odoo import models, fields


class Evento(models.Model):
    _name = "winamax_365.evento"
    _description = "Clase de evento deportivo"

    nombreEvento = fields.Char(string="Evento", required=True,
                               help="Ej.: Real Zaragoza - Huesca")
    deporteEvento = fields.Selection([
        ('futbol', 'Fútbol'),
        ('baloncesto', 'Baloncesto'),
        ('tenis', 'Tenis'),
        ('motor', 'Motor'),
        ('otros', 'Otros'),
    ], string="Deporte", default='futbol')
    fechaEvento = fields.Datetime(string="Fecha", default=fields.Datetime.now)
    enDirecto = fields.Boolean(string="En directo", default=False,
                               help="Marcado = apuesta en directo, sin marcar = pre-partido")
    cuotaEvento = fields.Float(string="Cuota", default=2.0,
                               help="Cuota de la apuesta")
