{
    'name': 'zapatos_ventas',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Registro y control de ventas de calzado',
    'depends': ['base', 'zapatos','mail'],  
    'data': [
        'security/ir.model.access.csv',
        'views/zapato_venta_views.xml',
    ],
    'installable': True,
    'application': True,
}