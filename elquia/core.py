"""
Edison Aguiar de Souza Neto
Natália Gama de Mattos
Pietro Gonçalves da Silva
"""

import os
import time
import random
import pygame

from utils import (
    abertura, fechamento, escolha_da_classe, pegar, ver_inventario,
    ver_estatistica, criar_jogador, ajuda, ver_sala, ir_para_sala,
    ver_direcao, batalha, procurar_itens, equipar_item, ver_npcs,
    ver_item, procurar_itens, DIRETORIO_ROOT
)

from npcs import npcs
from salas import salas
from inimigos import inimigos

def play_background_music():
    background_music = DIRETORIO_ROOT + '/resources/main_theme.ogg'
    pygame.mixer.init()
    pygame.mixer.music.load(background_music)
    pygame.mixer.music.play(loops=100)


def musica_de_batalha():
    musica = DIRETORIO_ROOT + '/resources/battle_song.ogg'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=100)

def musica_da_batalha_final():
    musica = DIRETORIO_ROOT + '/resources/final_battle_song.ogg'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=100)


def musica_de_fechamento():
    musica = DIRETORIO_ROOT + '/resources/final_song.ogg'
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play(loops=0)


comandos = [
    'pegar <item> | tudo',
    'ver inventario',
    'olhar sala',
    'ver <direção>',
    'ir <direção>',
    'procurar itens',
    'equipar <item>',
    'olhar item <item>',
    'procurar pessoas',
    'abrir',
    'escalar',
    'chutar',
    'ver jogador',
    'sair'
]

def run():
    play_background_music()
    abertura()

    # Começo do jogo

    jogador = criar_jogador()

    print("\nBem vindo a Élquia {}. Você tem exatamente {} items.\n".format(
                                jogador['nome'], len(jogador['inventario'])))

    print("Digite ajuda se precisar de ajuda.")
    print("O que você faz agora? ")
    ajuda(comandos)

    print("\nO reino de Élquia tem como público-alvo qualquer um que saiba ler.")

    # O jogador começa nos esgotos.
    jogador['sala_atual'] = salas['esgotos']

    while jogador['hp'] > 0 or jogador['vitoria'] == False:

        if (jogador['sala_atual']['nome'] == "Salão"
                and jogador['sala_atual']['batalhou'] == False):
            musica_de_batalha()
            batalha(jogador, inimigos['rato_gigante'])
            jogador['sala_atual']['batalhou'] = True
            play_background_music()

        elif (jogador['sala_atual']['nome'] == "Refeitório"
                and jogador['sala_atual']['batalhou'] == False):
            musica_de_batalha()
            batalha(jogador, inimigos['rato_gigante_refeitorio'])
            jogador['sala_atual']['batalhou'] = True
            play_background_music()

        elif (jogador['sala_atual']['nome'] == "Sala do trono"
                and jogador['sala_atual']['batalhou'] == False):

            musica_da_batalha_final()
            print(jogador['sala_atual']['falas'])
            time.sleep(3)
            opcoes_possives = ['sim', 'não']
            opcao = ''
            while opcao not in opcoes_possives:
                opcao = input("[Sim(se juntar ao rei Panteon) / Não(não se juntar ao rei Panteon)] ")
                opcao = opcao.lower().strip()

                if opcao == 'não':
                    print('''
                        Rei Panteon - Você não me deixa escolha, fale com
                        meus carrascos, tenho assuntos para cuidar no momento.
                        ''')
                elif opcao == 'sim':
                    print('''
                         Então você entende o que eu quero dizer. Para
                         seu último teste eu digo, derrote meu carrasco e seus
                         filhotes e então me encontre depois, se você for capaz
                         disto, eu saberei que você é forte o suficiente para
                         seguir meu legado, e a paz reinará de forma correta em
                         Élquia.
                    ''')
                time.sleep(3)
                batalha(jogador, inimigos['carrasco_do_rei_1'])
                batalha(jogador, inimigos['carrasco_do_rei_2'])
                batalha(jogador, inimigos['basilisco'])
                jogador['pontos'] += 150
                jogador['sala_atual']['batalhou'] = True
                jogador['vitoria'] = True
                print('''
                    Antes que você conseguisse alcançar o Rei Panteon, ele
                    já tinha fugido.
                    Agora é necessário ir  atrás de Panteon, temos negócios
                    inacabados aqui...
                ''')

                time.sleep(2)
                break

        if jogador['vitoria'] == True:
            break

        escolha = input("> ")
        escolha = escolha.lower().strip()

        if escolha.startswith("pegar"):
            try:
                item = escolha[5:].lower().strip()
                pegar(jogador, item)
            except:
                print("Item inválido.")

        elif escolha == "ajuda":
            ajuda(comandos)

        elif escolha == "olhar sala":
            ver_sala(jogador['sala_atual'])

        elif escolha.startswith("ir"):
            try:
                direcao = escolha[3:].lower().strip()
                if (jogador['sala_atual']['nome'] == "Porta da sala de controle"
                                    and direcao == "norte"):

                    # Ve se o jogador tem a chave da porta.
                    itens_do_jogador = ver_inventario(jogador, return_itens=True)
                    if "CHAVE DA PORTA DE CONTROLE" in itens_do_jogador:
                        jogador['sala_atual']['porta'] == 'aberta'
                        ir_para_sala(jogador, direcao)
                        ver_sala(jogador['sala_atual'])
                    else:
                        print("Você precisa da chave da porta.")

                elif (jogador['sala_atual']['nome'] == "Dormitório"
                                    and direcao == "norte"):

                    if jogador['sala_atual']['porta'] == 'fechada':
                        print("Há apenas um armário aqui...\n")
                    else:
                        ir_para_sala(jogador, direcao)
                        ver_sala(jogador['sala_atual'])

                elif (jogador['sala_atual']['nome'] == "Entrada do laboratório"
                                    and direcao == "oeste"):

                    itens_do_jogador = ver_inventario(jogador, return_itens=True)
                    if "Mão morta" in itens_do_jogador:
                        jogador['sala_atual']['porta'] == 'aberta'
                        ir_para_sala(jogador, direcao)
                        ver_sala(jogador['sala_atual'])
                    else:
                        print("Você não tem o que é necessário para abrir a porta...\n")

                elif (jogador['sala_atual']['nome'] == "Porta da sala de controle" and
                      direcao == "norte"):

                    itens_do_jogador = ver_inventario(jogador, return_itens=True)
                    if "CHAVE DA PORTA DE CONTROLE" in itens_do_jogador:
                        jogador['sala_atual']['porta'] == 'aberta'
                        ir_para_sala(jogador, direcao)
                        ver_sala(jogador['sala_atual'])
                    else:
                        print("Você não tem o que é necessário para abrir a porta...\n")

                elif (jogador['sala_atual']['nome'] == "Entrada do corredor de controle"
                                    and direcao == "oeste"):

                    itens_do_jogador = ver_inventario(jogador, return_itens=True)
                    if "CHAVE DO ELEVADOR" in itens_do_jogador:
                        ir_para_sala(jogador, direcao)
                        ver_sala(jogador['sala_atual'])
                    else:
                        print("Você não tem o que é necessário para abrir a porta...\n")
                else:
                    ir_para_sala(jogador, direcao)
                    ver_sala(jogador['sala_atual'])
            except:
                print("Direção inválida.")

        elif escolha.startswith("abrir"):
            try:
                abrir_oque = escolha[5:].lower().strip()
                if abrir_oque == "armario" or abrir_oque == "armário":
                    if jogador['sala_atual']['nome'] == "Dormitório":
                        jogador['sala_atual']['porta'] = 'aberta'
                        print("Você abriu uma porta.")

                elif abrir_oque == "porta":
                    if (jogador['sala_atual']['nome'] == "Porta da sala de controle" and
                        jogador['sala_atual']['porta'] == 'fechada'):

                        itens_do_jogador = ver_inventario(jogador, return_itens=True)
                        if "CHAVE DA PORTA DE CONTROLE" in itens_do_jogador:
                            jogador['sala_atual']['porta'] == 'aberta'
                            print("A porta foi aberta.")
                        else:
                            print("Você não tem o que é necessário para abrir a porta...\n")

                    elif (jogador['sala_atual']['nome'] == "Entrada do corredor de controle" and
                          jogador['sala_atual']['porta'] == 'fechada'):

                        itens_do_jogador = ver_inventario(jogador, return_itens=True)
                        if "CHAVE DO ELEVADOR" in itens_do_jogador:
                            jogador['sala_atual']['porta'] = 'aberta'
                            print("A porta foi aberta.")
                        else:
                            print("Você não tem o que é necessário para abrir a porta...\n")

                    elif (jogador['sala_atual']['nome'] == "Entrada do laboratório" and
                          jogador['sala_atual']['porta'] == 'fechada'):

                        itens_do_jogador = ver_inventario(jogador, return_itens=True)
                        if "Mão morta" in itens_do_jogador:
                            jogador['sala_atual']['porta'] == 'aberta'
                            print("A porta foi aberta.")
                        else:
                            print("Você não tem o que é necessário para abrir a porta...\n")

                else:
                    print("Nada para abrir aqui aqui.")
            except:
                print("Nada para abrir aqui aqui.")

        elif escolha == "usar poção":
            print("Você só pode usar as poções durante a batalha.")

        elif escolha == "procurar itens":
            procurar_itens(jogador['sala_atual'])

        elif escolha.startswith("ver"):
            try:
                direcao = escolha[3:].lower().strip()
                if direcao == 'inventario' or direcao == 'inventário':
                    ver_inventario(jogador)

                elif direcao == "jogador":
                    ver_estatistica(jogador)

                else:
                    ver_direcao(jogador['sala_atual'], direcao)
            except:
                print("Direção inválida.")

        elif escolha.startswith("olhar item"):
            try:
                item = escolha[10:].lower().strip()
                ver_item(jogador, item)
            except:
                print("Item inválido.")

        elif escolha.startswith("equipar"):
            try:
                item = escolha[7:].lower().strip()
                equipar_item(jogador, item)
            except:
                print("Item inválido.")

        elif escolha == "procurar pessoas":
            npc = ver_npcs(jogador['sala_atual'])
            time.sleep(1)
            if npc == "Cozinheiro" and npcs['cozinheiro']['hp'] > 0:
                print('''
                    Eu me aproximo do cozinheiro e pergunto algumas coisas
                    sobre a base, ele então implora por piedade, ele não
                    tem nenhuma informação para dar, ele faz parte apenas
                    dos funcionários de baixo nível.
                ''')
                # Poupar ou matar.
                opcoes_possives = ['poupar', 'matar']
                opcao = ''
                time.sleep(1)
                while opcao not in opcoes_possives:
                    opcao = input("Você vai poupar ou matar o cozinheiro? ")
                    opcao = opcao.lower().strip()

                    if opcao == "poupa":
                        print("Você decide poupar o pobre cozinheiro.")
                        jogador['pontos'] += 100
                    elif opcao == "matar":
                        print("Você decide acabar com a vida do pobre cozinheiro.")
                        npcs['cozinheiro']['hp'] = 0
                        jogador['pontos'] += 10

            elif npc == "Samantha" and npcs['samantha']['solta'] == False:
                print('''
                    Você vê uma menininha presa em uma gaiola.
                    Samantha - Por favor, me ajude, eles fizeram algo
                    com papai, me ajuda, eu não sei o que fazer.
                ''')
                opcoes_possives = [
                    'quebrar gaiola',
                    'chutar gaiola',
                    'arrebentar gaiola',
                    'libertar',
                    'libertar samantha',
                    'soltar',
                    'soltar samantha',
                    'abrir gaiola',
                    'deixar samantha',
                    'nada',
                    'sair'
                ]
                opcao = ''
                time.sleep(1)
                while opcao not in opcoes_possives:
                    opcao = input("O que você vai fazer? ")

                    if (opcao == opcoes_possives[0] or
                        opcao == opcoes_possives[1] or
                        opcao == opcoes_possives[2] or
                        opcao == opcoes_possives[3] or
                        opcao == opcoes_possives[4] or
                        opcao == opcoes_possives[5] or
                        opcao == opcoes_possives[6] or
                        opcao == opcoes_possives[7]):
                        print('''
                            Obrigada, eu ainda não sei o que fazer com papai,
                            mas obrigada, não sei se ajuda, mas os homens
                            maus costumavam desaparecer nos armários quando
                            eu estava com papai nos dormitórios, espero que
                            isso ajude.
                        ''')
                        npcs['samantha']['solta'] = True
                        jogador['pontos'] += 50
                    elif (opcao == opcoes_possives[8] or
                          opcao == opcoes_possives[9] or
                          opcao == opcoes_possives[10]):
                        print('''
                            Você decide deixar a probre garota encarcerada,
                            provavelmente até sua morte.
                        ''')
                        jogador['pontos'] -= 50

        elif escolha == "ver jogador":
            ver_estatistica(jogador)

        elif escolha.startswith("ver item"):
            try:
                item = escolha[8:].lower().strip()
                ver_item(jogador, item)
            except:
                print("Item inválido.")

        elif escolha == "escalar":
            if jogador['sala_atual']['nome'] == "Entrada do laboratório":
                print("Escalando...")
                time.sleep(1)
                pegar(jogador, "tudo")
            else:
                print("Nada para escalar aqui.")

        elif escolha.startswith("chutar") or escolha == "desativar reator":
            if jogador['sala_atual']['nome'] == "Base do núcleo térmico":
                if escolha.startswith("chutar"):
                    print('''
                        Você se prepara e começar a chutar contra o reator, ele
                        então toma um surto de energia e causa uma grande explosão!
                    ''')
                else:
                    print('''
                        Você se aproxima do reator e vê alguns paineis de controle,
                        coisa realmente antiga e com uma linguagem que você não
                        compreende, e então, aperta alguns botões aleatóriamente
                        até que então o reator começa a fazer um barulho estranho
                        parece que ele.. desativou? A sala então, fica
                        completamente no escuro.
                    ''')

        elif escolha == "sair":
            print("Saindo...\n")
            time.sleep(1)
            exit()

        else:
            print("Eu não te entendi!\n")


    if jogador['hp'] <= 0:
        print("Você morreu!")
        print("Você fez {} pontos".format(jogador['pontos']))
    elif jogador['vitoria'] == True:
        musica_de_fechamento()

        print("Você fez {} pontos".format(jogador['pontos']))
        if jogador['pontos'] >= 250:
            nomeacao = "campeão"
        elif jogador['pontos'] >= 150:
            nomeacao = "herói"
        elif jogador['pontos'] < 150:
            nomeacao = "lutador"

        print("Você é agora o {} de Élquia".format(nomeacao))
        time.sleep(2.5)
        fechamento()


if __name__ == '__main__':
    run()
