{
    'name': 'Zapatos Proveedores (Módulo Hijo)',
    'version': '1.0',
    'author': 'Isaac Campaña',
    'category': 'Sales',
    'summary': 'Administra la información de los proveedores relacionados con los productos del módulo principal.',
    'depends': [
        'base',
        'zapatos', 
    ],
    'data': [
        'views/zapato_views.xml',
    ],
    'installable': True,
    'application': False, 
    'license': 'LGPL-3',
}