{
    'name': "Winamax 365",
    'summary': "Apuestas deportivas y casino online",
    'description': """
        Módulo para gestionar una casa de apuestas online:
        jugadores, eventos deportivos, apuestas y juegos de casino.
    """,
    'author': "Raul",
    'website': "",
    'category': "Tools",
    'version': '1.1',
    'license': 'LGPL-3',
    'depends': ['base'],

'data': [
    'security/ir.model.access.csv',
    'views/usuario_view.xml',
    'views/evento_view.xml',
    'views/apuesta_view.xml',
    'views/juego_view.xml',
    'demo/demo.xml',
],

    'installable': True,
    'application': True,
}
