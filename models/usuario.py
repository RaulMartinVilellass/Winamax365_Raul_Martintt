from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Usuario(models.Model):
    _name = "winamax_365.usuario"
    _description = "Clase de usuario"

    nombreUsuario = fields.Char(string="Nombre", required=True,)
    apellidoUsuario = fields.Char(string="Apellido", required=True,)
    edadUsuario = fields.Integer(string="Edad", default=18,)
    saldoUsuario = fields.Float(string="Saldo (€)", default=0.0,)
    limiteDeposito = fields.Float(string="Límite de depósito (€)",)
    autoexcluido = fields.Boolean(string="Autoexcluido", default=False,)

    @api.constrains("edadUsuario")
    def _comprobar_edad(self):
        for u in self:
            if u.edadUsuario < 18:
                raise ValidationError("El usuario debe ser mayor de 18 años.")
