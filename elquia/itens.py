"""
Natália Gama, Edison Neto, Pietro Gonçalves
This software is a text RPG.

Copyright (C) 2018 Pietro Gonçalves
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

itens = {
     'adaga': {
        'nome': 'Adaga',
        'dano': 6.5,
        'valor': 0,
        'tipo': 'arma',
        'equipavel': False
    },

    'espada': {
        'nome': 'Espada',
        'dano': 10,
        'valor': 0,
        'tipo': 'arma',
        'equipavel': False
    },

    'faca': {
        'nome': 'Faca',
        'dano': 7.5,
        'valor': 10,
        'tipo': 'arma',
        'equipavel': False
    },
    'chave_da_porta_de_controle': {
        'nome': 'CHAVE DA PORTA DE CONTROLE',
        'dano': 0,
        'valor': 0,
        'tipo': 'arma',
        'equipavel': False
    },
    'arco': {
        'nome': 'Arco',
        'dano': 9,
        'valor': 10,
        'tipo': 'arma',
        'equipavel': False
    },
    'pingente_de_escudo': {
        'nome': 'Pingente de escudo',
        'dano': 0,
        'efeito': '+20HP',
        'valor': 30,
        'tipo': 'arma',
        'equipavel': True
    },
    'chave_do_elevador': {
        'nome': 'CHAVE DO ELEVADOR',
        'dano': 0,
        'valor': 0,
        'equipavel': False
    },
    'seringa_de_cura': {
        'nome': 'Seringa de cura',
        'dano': 0,
        'valor': 0,
        'tipo': 'arma',
        'equipavel': False
    },
    'mao_morta': {
        'nome': "Mão morta",
        "dano": 0,
        "valor": 0,
        'tipo': 'arma',
        'equipavel': False
    },
    "prototipo_de_faca_envenenada": {
        "nome": "Protótipo de faca envenenada",
        "dano": 12,
        "valor": 15,
        'tipo': 'arma',
        'equipavel': False
    },
    "pocao_de_vida": {
        "nome": "Poção de vida",
        "dano": 0,
        "valor": 50,
        "efeito": "+50hp",
        'tipo': 'pocao',
        'equipavel': False
    },
    'pocao_de_mana': {
        'nome': 'Poção de mana',
        'dano': 0,
        'valor': 50,
        'efeito': '+50mp',
        'tipo': 'pocao',
        'equipavel': False
     }
}
