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

from npcs import npcs
from itens import itens

NADA = ['Nada']

salas = {
    "esgotos": {
        'nome': 'Esgotos',
        'norte': ['Salão', "salao"],
        'sul': NADA,
        'leste': ['Passagem fechada', 'passagem_fechada'],
        'oeste': ['Almoxerifado', 'almoxerifado'],
        'descricao': '''
            Você está em um esgoto com túneis circulares, água
            escorrendo pelas paredes e com um cheiro forte de
            corpos pútridos.
        ''',
        'itens': []
    },
    "almoxerifado": {
        'nome': "Almoxerifado",
        'norte': NADA,
        'sul': ['Esgotos', "esgotos"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você entra em um almoxerifado, você não encontra nada
            além de vassouras e baldes de madeira.
        ''',
        'itens': [itens['pocao_de_vida'], itens['pocao_de_mana']],
    },
    "salao": {
        'nome': 'Salão',
        'norte': ['Porta da sala de controle', "porta_sala_de_controle"],
        'sul': ['Dormitório', "dormitorio"],
        'leste': ['Sala de espécies', "sala_especies"],
        'oeste': ['Refeitório', "refeitorio"],
        'descricao': '''
            A porta que te levou até essa sala fecha, e você
            se encontra em um grande salão, porém completamente
            vazio, este mesmo possui três pilares de sustentação que
            aparentemente só serve para a decoração deste grande lobby
            para indicar que existem 3 passagens.
        ''',
        'itens': [],
        'batalhou': False
    },
    "refeitorio": {
        'nome': 'Refeitório',
        'norte': ['Cozinha', 'cozinha'],
        'sul': ['Salão', 'salao'],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você está em um refeitório, para uma base militar
            de ratos aqui parece limpo até demais, mas nada além do
            que uma sala vazia.
        ''',
        'itens': [],
        'batalhou': False
    },
    "cozinha": {
        'nome': 'Cozinha',
        'norte': NADA,
        'sul': ['Refeitório', "refeitorio"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Uma cozinha comum, um pouco menos limpa que o refeitório,
            mas ainda sim, um lugar interessante para um bom fã
            de gastronomia.
        ''',
        'itens': [
            itens['faca'],
            itens['pocao_de_vida'],
            itens['pocao_de_mana']
        ],
        "npcs": npcs['cozinheiro']
    },
    "porta_sala_de_controle": {
        'nome': 'Porta da sala de controle',
        'norte': [
            "Entrada do corredor de controle",
            "entrada_corredor_de_controle"
            # Para entrar nesta sala, será necessário.
            # uma CHAVE DA PORTA DE CONTROLE.
        ],
        'sul': ['Salão', "salao"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você dá de cara com uma grande porta de metal, ela
            não possui maçaneta, mas é possível observar um painel
            com entrada para uma chave na parede a esquerda desta porta.
        ''',
        'itens': [],
        'porta': 'fechada'
    },
    "sala_especies": {
        'nome': 'Sala de espécies',
        'norte': NADA,
        'sul': ['Porta da sala de controle', 'porta_sala_de_controle'],
        'leste': ['Passagem Fechada', 'passagem_fechada'],
        'oeste': ['Salão', "salao"],
        'descricao': '''
            Você entra em uma sala de espécies, aparentemente ela possui
            esse nome mas não passa de uma sala de aprisionamento de
            escravos, você vê ratos genéticamente modificados de forma
            defeituosa, aparentemente guardam os testes falhos aqui,
            você observa também uma criança chorando dentro de uma
            gaiola com um rato defeituoso ao lado.
        ''',
        'npcs': npcs['samantha'],
        'itens': []
    },
    "passagem_fechada": {
        'nome': 'Passagem fechada',
        'norte': NADA,
        'sul': NADA,
        'leste': NADA,
        'oeste': ['Sala de espécies', 'sala_especies'],
        'descricao': '''
            Você encontra um monte de escombros de pedra
            fechando uma passagem.
        ''',
        'itens': [itens['pocao_de_vida'], itens['pocao_de_mana']],
    },
    "dormitorio": {
        'nome': "Dormitório",
        'norte': ['Salão', "salao"],
        'sul': ['Porta da sala de controle', 'porta_sala_de_controle'],
        'leste': ['Armário', "sala_do_chefe"],
        'oeste': NADA,
        'descricao': '''
            Você entra em um dormitório de soldados, você vê camas
            pouco confortáveis e um armário ao fundo, provavelmente
            guardam roupas comuns de soldados.
        ''',
        'itens': [itens['arco'], itens['pocao_de_mana']],
        'porta': 'fechada'
    },
    "sala_do_chefe": {
        'nome': 'Sala do chefe',
        'norte': NADA,
        'sul': ['Dormitório', 'dormitorio'],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você entra em uma sala um pouco menor, que faz juz
            a passagem apertada que você teve que passar, na sua
            frente você vê uma pequena mesa com uma chave, aparentemente
            importante e algumas anotações.
        ''',
        'itens': [itens['chave_da_porta_de_controle'], itens['pingente_de_escudo']],
    },
    "entrada_corredor_de_controle": {
        'nome': "Entrada do corredor de controle",
        'norte': ['Sala de armas', "sala_de_armas"],
        'sul': ['Porta da sala de controle', "porta_sala_de_controle"],
        'leste': ['Sala de controle', "sala_de_controle"],
        'oeste': ['Entrada do elevador', "entrada_do_elevador"],
        'descricao': '''
            Você está em um corredor, você vê várias entradas, precisa
            escolher para onde ir.
        ''',
        'itens': [],
        'porta': 'fechada'
    },
    "sala_de_armas": {
        'nome': 'Sala de armas',
        'norte': NADA,
        'sul': [
            'Entrada do corredor de controle',
            "entrada_corredor_de_controle"
        ],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você esta em uma sala de armas comuns, nada melhor do que
            você já tenha, mas algo brilhando te chama a atenção.
        ''',
        'itens': [itens['pocao_de_vida'], itens['pocao_de_mana']]
    },
    "sala_de_controle": {
        'nome': "Sala de controle",
        'norte': NADA,
        'sul': [
            'Entrada do corredor de controle',
            "entrada_corredor_de_controle"
        ],
        'leste': ['Núcleo térmico da base no esgoto', 'nucleo_termico'],
        'oeste': NADA,
        'descricao': '''
            Em uma sala de controle, você se estranha de logo a pouco
            estar em um esgoto nojento, tecnologia contando mais sobre
            a Arcus e suas pesquisas te impressionam o quão longe isto
            está indo, mais a frente em uma passagem você vê um brilho
            esverdeado.
            Logo encima de uma das mesinhas, você vê outra chave, e uma
            espécie de seringa.
        ''',
        'itens': [
            itens['chave_do_elevador'],
            itens['seringa_de_cura']
        ]
    },
    "nucleo_termico": {
        'nome': "Núcleo térmico",
        'norte': NADA,
        'sul': ['Sala de controle', "sala_de_controle"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você se aproxima de algo que parece ser uma fonta de
            energia da base, aparentemente é para aqui que as almas
            estão indo após a morte daqueles pobres civis, ele parece
            muito resistente, logo atacá-lo será em vão.
        ''',
        'itens': []
    },
    "entrada_do_elevador": {
        'nome': "Entrada do elevador",
        'norte': ['Elevador (Subsolo)', "subsolo"],
        'sul': [
            'Entrada do coredor de controle',
            "entrada_corredor_de_controle"
        ],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            A sua frente tem um elevador velho que parece ter apenas
            um caminho, para um fundo fosso abaixo de você
        ''',
        'itens': []
    },
    "subsolo": {
        'nome': "Subsolo",
        'norte': ['Entrada do laboratório', "entrada_do_laboratorio"],
        'sul': ['Elevador (Primeiro andar)', "entrada_do_elevador"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você tem apenas um caminho, a volta por esse elevador
            velho rangente, ou seguir o corredor para um destino desconhecido.
        ''',
        'itens': [itens['pocao_de_vida'], itens['pocao_de_mana']]
    },
    "entrada_do_laboratorio": {
        'nome': "Entrada do laboratório",
        'norte': ['Base do núcleo térmico da base', "base_nucleo_termico"],
        'sul': ['Entrada do elevador', 'segundo_andar'],
        'leste': ['Sala de armas científicas', "sala_armas_cientificas"],
        'oeste': ['Laboratório', "laboratorio"],
        'descricao': '''
            Você está em uma sala gigante, o chão está chegando
            a quase tampar seu pé com água de esgoto, no centro
            da sala uma estátua de um troll petrificado com uma
            mão morta no pescoço usando como um colar e atrás do
            troll, um portão com um painel
        ''',
        'itens': [itens['mao_morta']],
        'porta': 'fechada'
    },
    "base_nucleo_termico": {
        'nome': "Base do núcleo térmico",
        'norte': NADA,
        'sul': ['Entrada do laboratório', "entrada_do_laboratorio"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você está na base do reator, o reator aqui faz a área parecer
            muito mais quente e densa, alguns civis ciêtistas estão
            assustados no fundo da sala choramingando em um canto
        ''',
        'itens': [itens['pocao_de_vida'], itens['pocao_de_mana']],
        'reator': 'ativado'
    },
    "sala_armas_cientificas": {
        'nome': "Sala de armas científicas",
        'norte': NADA,
        'sul': ['Entrada do laboratório', "entrada_do_laboratorio"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Uma sala de armas mas parecem que estas foram usadas em
            testes ciêntificos para se obter melhoras
        ''',
        'itens': [itens['prototipo_de_faca_envenenada']],
    },
    "laboratorio": {
        'nome': "Laboratório",
        'norte': ['Escadaria para sala do trono', "escadaria_sala_do_trono"],
        'sul': ['Entrada do laboratório', "entrada_do_laboratorio"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Você está em um laboratório gigante, parece que muitas
            pesquisas são feitas aqui, você não consegue entender
            muito a linguagem que passa aqui, mas sem dúvidas parece
            ser algo grande.
        ''',
        'itens': []
    },
    "escadaria_sala_do_trono": {
        'nome': "Escadaria para sala do trono",
        'norte': ['Sala do trono', "sala_do_trono"],
        'sul': ['Laboratório', "laboratorio"],
        'leste': NADA,
        'oeste': NADA,
        'descricao': 'Uma escadaria',
        'itens': [
            itens['pocao_de_vida'],
            itens['pocao_de_vida'],
            itens['pocao_de_mana'],
            itens['pocao_de_mana']
        ],
    },
    "sala_do_trono": {
        'nome': "Sala do trono",
        'norte': ['Saída secreta para Élquia', "saida_secreta_para_elquia"],
        'sul': ['Escadaria para sala do trono', 'escadaria_sala_do_trono'],
        'leste': NADA,
        'oeste': NADA,
        'descricao': '''
            Uma sala também gigante, as proporções parecem não parar
            de aumentar, vários pilares de energia como o gerador antes
            visto, mas versões menores dele e uma escadaria que dá
            para um altar de rei.
        ''',
        'falas' : '''
            Você entra na sala do trono e avista o rei Panteon
            Boa tarde, senhor, você é muito barulhento né? Causando tanta matança
            contra pessoas que apenas lutam pelos seus direitos.
            Rei Panteon - você acha que eu sou o errado nesta história?
            O seu rei tolo é o grande culpado nesta história.
            Nós dos esgotos, tinhamos um acordo com o rei de Elquia, porém ele
            se achou no direito de criar regras novas nessa federação sem nos contatar,
            regras que nos afetariam, então tivemos que fazer o que fizemos, peço perdão
            pelo equivoco.. Você compreende, não é?
        ''',
        #Se vencer a batalha, fale que o Panteon fugiu e que a trama não termina aqui, pois ainda tem muita coisa para lidar e ainda, encontrar Panteon#
        'itens': [],
        'batalhou': False
    }
}
