from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ZapatoVenta(models.Model):
    _name = 'zapatos.venta'
    _description = 'Registro de Ventas de Zapatos'

    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    zapato_id = fields.Many2one('zapatos.zapato', string='Producto (Zapato)', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1, required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    fecha_venta = fields.Date(string='Fecha de Venta', default=fields.Date.context_today, required=True)
    total = fields.Float(string='Total de Venta', compute='_compute_total', store=True)
    description = fields.Html(string='Notas internas')

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total(self):
        for record in self:
            record.total = record.cantidad * record.precio_unitario

    @api.onchange('zapato_id')
    def _onchange_zapato_id(self):
        if self.zapato_id:
            # Asumiendo que el modelo 'zapatos.zapato' tiene el campo 'precio'
            self.precio_unitario = self.zapato_id.precio

    @api.constrains('cantidad')
    def _check_cantidad(self):
        for record in self:
            if record.cantidad <= 0:
                raise ValidationError('¡Error! La cantidad de zapatos a vender debe ser mayor que cero.')

    @api.constrains('precio_unitario')
    def _check_precio(self):
        for record in self:
            if record.precio_unitario < 0:
                raise ValidationError('¡Error! El precio unitario no puede ser un valor negativo.')

    @api.constrains('fecha_venta')
    def _check_fecha(self):
        for record in self:
            if record.fecha_venta > fields.Date.today():
                raise ValidationError('¡Error! No puedes registrar una venta con una fecha del futuro.')