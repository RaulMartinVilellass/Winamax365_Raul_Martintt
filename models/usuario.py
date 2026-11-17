from datetime import date

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Usuario(models.Model):
    _name = "winamax_365.usuario"
    _description = "Jugador de Winamax 365"
    _rec_name = "nombreUsuario"
    _order = "apellidoUsuario, nombreUsuario"

    _sql_constraints = [
        ('saldo_positivo', 'CHECK("saldoUsuario" >= 0)', 'El saldo no puede ser negativo.'),
    ]

    nombreUsuario = fields.Char(string="Nombre", required=True)
    apellidoUsuario = fields.Char(string="Apellido", required=True)
    fechaNacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    edadUsuario = fields.Integer(string="Edad", compute="_calcular_edad", store=True)
    fechaRegistro = fields.Datetime(string="Fecha de registro", default=fields.Datetime.now, readonly=True)
    saldoUsuario = fields.Float(string="Saldo (€)", default=0.0)
    limiteDeposito = fields.Float(string="Límite de depósito (€)")
    autoexcluido = fields.Boolean(string="Autoexcluido", default=False)
    foto = fields.Binary(string="Foto")
    notasUsuario = fields.Text(string="Notas internas")
    nivelUsuario = fields.Selection([('bronce', 'Bronce'), ('plata', 'Plata'), ('oro', 'Oro')], string="Nivel", default='bronce')
    emailUsuario = fields.Char(string="Correo electrónico")
    telefonoUsuario = fields.Char(string="Teléfono")

    apuesta_ids = fields.One2many("winamax_365.apuesta", "usuario_id", string="Apuestas")
    juego_ids = fields.Many2many("winamax_365.juego", relation="winamax_usuario_juego_rel",column1="usuario_id", column2="juego_id",string="Juegos favoritos")

    @api.depends('fechaNacimiento')
    def _calcular_edad(self):
        hoy = date.today()
        for u in self:
            try:
                n = u.fechaNacimiento

                u.edadUsuario = hoy.year - n.year - ((hoy.month, hoy.day) < (n.month, n.day))
            except AttributeError:
                u.edadUsuario = 0

    @api.constrains('fechaNacimiento')
    def _comprobar_edad(self):
        for u in self:
            if u.edadUsuario < 18:
                raise ValidationError("El usuario debe ser mayor de 18 años.")
