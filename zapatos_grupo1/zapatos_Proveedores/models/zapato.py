from odoo import models, fields, api

class ZapatoProveedor(models.Model):
    # Heredamos el modelo del módulo padre tal como lo pide el enunciado
    _inherit = 'zapatos.zapato'

    # Incorporación de los nuevos campos solicitados
    proveedor_nombre = fields.Char(string='Nombre del Proveedor', required=True)
    proveedor_telefono = fields.Char(string='Teléfono')
    proveedor_correo = fields.Char(string='Correo Electrónico')
    fecha_adquisicion = fields.Date(string='Fecha de Adquisición', default=fields.Date.context_today)
    costo_compra = fields.Float(string='Costo de Compra ($)', default=0.0)