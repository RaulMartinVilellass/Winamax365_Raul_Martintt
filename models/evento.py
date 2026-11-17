from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Evento(models.Model):
    _name = "winamax_365.evento"
    _description = "Evento deportivo"
    _rec_name = "nombreEvento"
    _order = "fechaEvento desc"

    nombreEvento = fields.Char(string="Evento", required=True)
    deporteEvento = fields.Selection([('futbol', 'Fútbol'), ('baloncesto', 'Baloncesto'), ('tenis', 'Tenis'), ('motor', 'Motor'), ('otros', 'Otros')], string="Deporte", default='futbol')
    estadoEvento = fields.Selection([('programado', 'Programado'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado')], string="Estado", default='programado')
    fechaEvento = fields.Datetime(string="Fecha y hora", default=fields.Datetime.now)
    imagenEvento = fields.Binary(string="Imagen")
    cuotaEvento = fields.Float(string="Cuota", default=2.0)
    totalApuestas = fields.Integer(string="Nº de apuestas", compute="_calcular_totales", store=True)

    apuesta_ids = fields.One2many("winamax_365.apuesta", "evento_id", string="Apuestas")

    @api.depends('apuesta_ids')
    def _calcular_totales(self):
        for e in self:
            e.totalApuestas = len(e.apuesta_ids)

    @api.constrains('cuotaEvento')
    def _comprobar_evento(self):
        for e in self:
            if e.cuotaEvento <= 1:
                raise ValidationError("La cuota debe ser mayor que 1.")
