from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Apuesta(models.Model):
    _name = "winamax_365.apuesta"
    _description = "Clase de apuesta"

    usuario_id = fields.Many2one("winamax_365.usuario", string="Usuario",
                                 required=True)
    evento_id = fields.Many2one("winamax_365.evento", string="Evento",
                                required=True)
    importeApuesta = fields.Float(string="Importe (€)", default=5.0)
    cuotaApuesta = fields.Float(string="Cuota", related="evento_id.cuotaEvento",
                                store=True)
    gananciaApuesta = fields.Float(string="Ganancia posible (€)",
                                   compute="_calcular_ganancia", store=True)
    estadoApuesta = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('ganada', 'Ganada'),
        ('perdida', 'Perdida'),
    ], string="Estado", default='pendiente')

    @api.depends('importeApuesta', 'cuotaApuesta')
    def _calcular_ganancia(self):
        for a in self:
            a.gananciaApuesta = a.importeApuesta * a.cuotaApuesta

    @api.constrains('importeApuesta', 'usuario_id')
    def _comprobar_apuesta(self):
        for a in self:
            if a.importeApuesta <= 0:
                raise ValidationError("El importe debe ser mayor que 0.")
            if a.usuario_id.autoexcluido:
                raise ValidationError("El jugador está autoexcluido.")

    def action_ganada(self):
        for a in self.filtered(lambda x: x.estadoApuesta == 'pendiente'):
            a.estadoApuesta = 'ganada'
            a.usuario_id.saldoUsuario += a.gananciaApuesta

    def action_perdida(self):
        for a in self.filtered(lambda x: x.estadoApuesta == 'pendiente'):
            a.estadoApuesta = 'perdida'

    @api.model_create_multi
    def create(self, vals_list):
        apuestas = super().create(vals_list)
        for a in apuestas:
            if a.usuario_id.saldoUsuario < a.importeApuesta:
                raise ValidationError("Saldo insuficiente.")
            a.usuario_id.saldoUsuario -= a.importeApuesta
        return apuestas
