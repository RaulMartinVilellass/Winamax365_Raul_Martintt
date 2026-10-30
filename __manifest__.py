# -*- coding: utf-8 -*-
{
    'name': "winamax_365",
    'summary': "Apuestas deportivas y casino online",
    'description': "Modulo sencillo: jugadores, eventos, apuestas y juegos de casino",
    'author': "Raul",
    'website': "",
    'category': "Tools",
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/usuario_view.xml',
        'views/evento_view.xml',
        'views/apuesta_view.xml',
        'views/juego_view.xml',
    ],

    'installable': True,
    'application': True,
}
