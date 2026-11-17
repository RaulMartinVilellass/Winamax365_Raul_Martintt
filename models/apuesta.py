from odoo import models, fields, api


class Apuesta(models.Model):
    _name = "winamax_365.apuesta"
    _description = "Apuesta"
    _rec_name = "referenciaApuesta"
    _order = "fechaApuesta desc"

    referenciaApuesta = fields.Char(string="Referencia", required=True, default="Apuesta nueva")
    importeApuesta = fields.Float(string="Importe (€)", default=5.0)
    cuotaApuesta = fields.Float(string="Cuota", readonly=True)
    gananciaApuesta = fields.Float(string="Ganancia posible (€)", compute="_calcular_ganancia", store=True)
    estadoApuesta = fields.Selection([('borrador', 'Borrador'), ('pendiente', 'Pendiente'), ('ganada', 'Ganada'), ('perdida', 'Perdida'), ('anulada', 'Anulada')], string="Estado", default='borrador')
    fechaApuesta = fields.Datetime(string="Fecha de la apuesta", default=fields.Datetime.now)
    fechaPago = fields.Date(string="Fecha de pago", readonly=True)
    justificante = fields.Binary(string="Justificante (imagen)")
    notasApuesta = fields.Text(string="Notas")
    tipoApuesta = fields.Selection([('simple', 'Simple'), ('combinada', 'Combinada'), ('sistema', 'Sistema')], string="Tipo de apuesta", default='simple')

    usuario_id = fields.Many2one("winamax_365.usuario", string="Jugador", required=True, ondelete="restrict")
    evento_id = fields.Many2one("winamax_365.evento", string="Evento", required=True, ondelete="restrict")

    @api.depends('importeApuesta', 'cuotaApuesta', 'evento_id.cuotaEvento')
    def _calcular_ganancia(self):
        for a in self:
            cuota = a.cuotaApuesta or a.evento_id.cuotaEvento
            a.gananciaApuesta = a.importeApuesta * cuota

