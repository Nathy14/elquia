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

import os
import time
import random

from magias import magias
from itens import itens
from salas import salas

DIRETORIO_ROOT = os.path.dirname(os.path.abspath(__file__))

def abertura():
    """Imprime o texto de abertura. """
    columns = os.get_terminal_size().columns

    texto = open('texto_de_abertura.txt', 'r')
    texto_de_abertura = texto.readlines()

    for line in texto_de_abertura:
        print(line.center(columns))
        time.sleep(3)

    texto.close()


def fechamento():
    print('''
        _      _____        _                                      _
       / \    |  ___|__  __| | ___ _ __ __ _  ___ __ _  ___     __| | ___
      / _ \   | |_ / _ \/ _` |/ _ \ '__/ _` |/ __/ _` |/ _ \   / _` |/ _ \
     / ___ \  |  _|  __/ (_| |  __/ | | (_| | (_| (_| | (_) | | (_| |  __/
    /_/   \_\ |_|  \___|\__,_|\___|_|  \__,_|\___\__,_|\___/   \__,_|\___|

     _____ _             _
    | ____| | __ _ _   _(_) __ _
    |  _| | |/ _` | | | | |/ _` |
    | |___| | (_| | |_| | | (_| |
    |_____|_|\__, |\__,_|_|\__,_|
                |_|

    ''')
    time.sleep(3)
    print("A federação de Élquia foi desenvolvido por:")
    print("Edison Aguiar de Souza Neto")
    time.sleep(2.5)
    print("Natália Gama de Mattos")
    time.sleep(2.5)
    print("Pietro Gonçalves da Silva")
    time.sleep(2.5)
    print('\n')
    time.sleep(118)


def mudar_nome_utf8(nome):
    nome = nome.lower()
    nome = nome.replace('ç', 'c')
    nome = nome.replace('ã', 'a')
    nome = nome.replace('á', 'a')
    nome = nome.replace('õ', 'o')
    nome = nome.replace('ó', 'o')
    nome = nome.replace('é', 'e')
    nome = nome.replace(' ', '_')

    return nome


def escolha_da_classe():
    """Essa funcao e usada para que o jogador possa escolher sua classe."""
    classes_possiveis = ["mago", "guerreiro", "ladino"]
    classe = ''
    while classe not in classes_possiveis:
        classe = input("Escolha sua classe[Mago/Guerreiro/Ladino]: ")
        classe = classe.lower().strip()

        # Os atributos mudam conforme a classe.
        if classe == "mago":
            hp = 100
            mp = 200
            forca = 10
        elif classe == "guerreiro":
            hp = 200
            mp = 100
            forca = 20
        elif classe == "ladino":
            hp = 150
            mp = 150
            forca = 15
        else:
            print("Classe inválida")

    # Retorna a classe, o hp e a mp em variaveis diferentes.
    return classe, hp, mp, forca


def pegar(jogador, item):
    """Pega um devido item. """
    try:
        if item == "tudo":
            itens_na_sala = jogador['sala_atual']['itens']
            # Mensagem caso não haja itens.
            if len(itens_na_sala) <= 0:
                print("Sem itens aqui.")
                return None

            for item in itens_na_sala:
                jogador['inventario'].append(item)
            del jogador['sala_atual']['itens'][:]
            print("Você pegou todos os itens da sala.")
        else:
            item = mudar_nome_utf8(item)
            item = itens[item]
            itens_na_sala = jogador['sala_atual']['itens']
            # Mensagem caso não haja itens.
            if len(itens_na_sala) <= 0:
                print("Sem itens aqui.")
                return None

            for index, item_na_sala in enumerate(itens_na_sala):
                if item == item_na_sala:
                    jogador['inventario'].append(item)
                    del jogador['sala_atual']['itens'][index]
            print("Você pegou {}".format(item['nome']))
    except:
        print("Não há item para ser pego.")


def ver_inventario(jogador, return_itens=False):
    """Imprime os itens no inventario do jogador. """
    if not return_itens:
        print("\nTotal de itens: {}".format(len(jogador['inventario'])))
        print("Seus itens: \n")
    nome_dos_itens = []
    for item in jogador['inventario']:
        if not return_itens:
            print(item['nome'])
        nome_dos_itens.append(item['nome'])

    if return_itens:
        return nome_dos_itens


def ver_item(jogador, item):
    for itens in jogador['inventario']:
        if itens['nome'] == item:
            print(item)


def ver_estatistica(jogador):
    print("Nome: {}".format(jogador['nome']))
    print("Classe: {}".format(jogador['classe']))
    print("Vida: {}".format(jogador['hp']))
    print("Mana: {}".format(jogador['mp']))
    print("Força: {}".format(jogador['forca']))
    print("Pontos: {}".format(jogador['pontos']))

def criar_jogador():
    nome = input("Qual o seu nome: ")
    classe, hp, mp, forca = escolha_da_classe()

    jogador = {
        'nome': nome,
        'classe': classe,
        'hp': hp,
        'maxhp': hp,
        'mp': mp,
        'maxmp': mp,
        'forca': forca,
        'inventario': [itens["pocao_de_vida"],itens["pocao_de_vida"]],
        'sala_atual': '',
        'vitoria': False,
        'pontos': 0,
        'item_equipado': itens['faca']
    }

    # Mago começa com magias no inventário.
    if classe == "mago":
        jogador['inventario'].append(magias['bola_de_fogo'])
        jogador['inventario'].append(magias['abraco_gelido'])
        jogador['inventario'].append(magias['nevoa_acida'])
        jogador['inventario'].append(itens['pocao_de_mana'])
        jogador['inventario'].append(itens['pocao_de_mana'])
    # Guerreiro começa com uma espada no iventário.
    elif classe == 'guerreiro':
        jogador['inventario'].append(itens['espada'])
    # Ladino começa com uma magia e uma adaga no iventário.
    elif classe == 'ladino':
        jogador['inventario'].append(magias['mutilar'])
        jogador['inventario'].append(itens['adaga'])
        jogador['inventario'].append(itens['pocao_de_mana'])
        jogador['inventario'].append(itens['pocao_de_mana'])

    return jogador


def ajuda(comandos):
    print("\nAções possíveis: \n")
    for acao in comandos:
        print(acao)

    print("\nDireções: ")
    print("Norte, Sul, Leste, Oeste")


def ver_direcao(sala, direcao):
    print("{}".format(sala[direcao][0]))


def ver_sala(sala):
    print("{}".format(sala["descricao"]))

def equipar_item(jogador, item):
    if len(jogador['inventario']) > 0:
        item = mudar_nome_utf8(item)
        if jogador['item_equipado'] == item:
            print("Este item já está equipado.")
            return None

        if item['equipavel'] == False:
            print("Item inequipável")
            return None

        if jogador['item_equipado']['nome'] == "Pingente de escudo":
            jogador['hp'] += 20
            jogador['maxhp'] += 20

        print("Item equipado")
    else:
        print("Você não tem nenhum item!")


def procurar_itens(sala):
    try:
        for item in sala['itens']:
            print("{}".format(item['nome']))
    except:
        print("Sem itens aqui!")


def ver_npcs(sala):
    try:
        if sala['npcs']['hp'] <= 0:
            print("Cadáver do {}.".format(salas['npcs']['nome']))
        else:
            print(sala['npcs']['nome'])
        return sala['npcs']['nome']
    except:
        print("Sem pessoas aqui!")


def ir_para_sala(jogador, direcao):
    try:
        nova_sala = jogador['sala_atual'][direcao][1]
        jogador['sala_atual'] = salas[nova_sala]
    except:
        print("Você não pode ir para esse lugar.")


def batalha(jogador, inimigo):
    print("\nQuando você entra na sala um " + inimigo['nome'] + " te ataca.")
    print("Você revida.\n")
    time.sleep(1)
    while jogador['hp'] > 0 or inimigo['hp'] > 0:

        # Escolha do item/magia para atacar.
        print('\n')
        numeros_possiveis = []
        if len(jogador['inventario']) > 0:
            for index, item in enumerate(jogador['inventario']):
                if item['tipo'] == 'arma':
                    print("{}: {}, Dano: {}".format(
                                            index, item['nome'], item['dano']))
                elif item['tipo'] == 'pocao':
                    print("{}: {}, Efeito: {}".format(
                                            index, item['nome'], item['efeito']))
                else:
                    print("{}: {}, Dano: {}, Mana: {}".format(
                                            index, item['nome'], item['dano'],
                                            item['mp']))

                numeros_possiveis.append(index)

        arma_escolhida = ''
        while arma_escolhida not in numeros_possiveis:
            try:
                arma_escolhida = int(input("\nEscolha sua forma de ataque[número]: "))
            except:
                print("O valor tem que corresponder com um dos itens.")


        stats_arma = list(enumerate(jogador['inventario']))[arma_escolhida][1]

        # Dano da arma escolhida.
        if stats_arma['dano'] > 0:
            dano_escolhido = stats_arma['dano']

            # Consumo de mp.
            if stats_arma['tipo'] == 'magia':
                nome_da_magia = mudar_nome_utf8(stats_arma['nome'])
                if (jogador['mp'] - magias[nome_da_magia]['mp']) >= 0:
                    dano_escolhido = stats_arma['dano']
                    jogador['mp'] -= magias[nome_da_magia]['mp']
                else:
                    print("Mana insuficiente.")
                    dano_escolhido = 0
        else:
            try:
                efeito = stats_arma['efeito']
                # Se a vida do jogador for ficar maior do que a vida maxima dele.
                if efeito == '+50hp':
                    if (jogador['hp'] + 50) > jogador['maxhp']:
                        jogador['hp'] = jogador['maxhp']
                        print("Vida restorada ou máximo.")
                    else:
                        jogador['hp'] += 50
                        print("Restorado 50 pontos de vida.")
                else:
                    if (jogador['mp'] + 50) > jogador['maxmp']:
                        jogador['mp'] = jogador['maxmp']
                        print("Mana restorada ou máximo.")
                    else:
                        jogador['mp'] += 50
                        print("Restorado 50 pontos de mana.")


                # Deleta a poção do inventário depois de usuada.
                del jogador['inventario'][arma_escolhida]
                dano_escolhido = 0
            except:
                print("\nVocê escolhe lutar desarmado...")
                dano_escolhido = 5


        dano = jogador['forca'] * random.uniform(0.0, 0.5)
        dano_do_jogador = dano_escolhido + dano

        dano_do_inimigo = inimigo['dano']

        jogador['hp'] -= dano_do_inimigo
        inimigo['hp'] -= dano_do_jogador

        print("\nVocê deu {:.1f} de dano, e sofreu {}".format(dano_do_jogador,dano_do_inimigo))
        print("Você possui {:.1f} de vida".format(jogador['hp']))
        print("O inimigo possui {:.1f}".format(inimigo['hp']))
        print("Você possui {} de mana".format(jogador['mp']))

        time.sleep(1)

        if inimigo['hp'] <= 0:
            print("\nO inimigo morreu!\n")
            cinquenta_vida = jogador['maxhp'] * .5
            um_quarto_vida = jogador['maxhp'] * .25
            # Dependendo da quantidade de vida o jogador ganha mais pontos.
            if jogador['hp'] > cinquenta_vida:
                jogador['pontos'] += 50
                jogador['forca'] += 2
            elif jogador['hp'] > um_quarto_vida:
                jogador['pontos'] += 25
                jogador['forca'] += 1
            else:
                jogador['pontos'] += 10

            time.sleep(1)
            break

        elif jogador['hp'] <= 0:
            print("Você morreu")
            time.sleep(1)
            exit()
        else:
            print("A batalha continua...")

        time.sleep(3)
