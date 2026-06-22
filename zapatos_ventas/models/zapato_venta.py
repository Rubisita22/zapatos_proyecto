from odoo import api, fields, models

class ZapatoVenta(models.Model):
    _name = 'zapatos.venta'
    _description = 'Registro de Ventas de Zapatos'
    cliente_id = fields.Many2one('res.partner', string='Cliente', required=True)
    zapato_id = fields.Many2one('zapatos.zapato', string='Producto (Zapato)', required=True)
    cantidad = fields.Integer(string='Cantidad', default=1, required=True)
    precio_unitario = fields.Float(string='Precio Unitario', required=True)
    fecha_venta = fields.Date(string='Fecha de Venta', default=fields.Date.context_today, required=True)
    total = fields.Float(string='Total de Venta', compute='_compute_total', store=True)

    @api.depends('cantidad', 'precio_unitario')
    def _compute_total(self):
        for record in self:
            record.total = record.cantidad * record.precio_unitario

    @api.onchange('zapato_id')
    def _onchange_zapato_id(self):
        if self.zapato_id:
            self.precio_unitario = self.zapato_id.precio