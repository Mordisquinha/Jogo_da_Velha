from random import randrange
from time import sleep

# rafael cuzao

corpo = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]
contador_velha = 1
jogador = 0


def bem_vindo(): #layout de entrada

    print('{:#^100}'.format(' Jogo da Velha '))
    start = input('press "s" to start: ')
    if start == 's':
        primeiro()
    while start != 's':
        print('Only press "s" ass hole')
        start = input('press "s" to start: ')
        if start == 's':
            primeiro()


def primeiro(): #Sorteio do Primeiro Jogador
    global jogador
    print('Vamos ver quem irá começar o jogo')
    for p in range(0, 3):
        sleep(0.5)
        print('.', end='')
    jogador = randrange(0, 2)

    if jogador == 1:

        print('\nVocê começa! ')
        sleep(0.5)
        print("""    linha, coluna                  
['0,0', '0,1', '0,2']
['1,0', '1,1', '1,2']
['2,0', '2,1', '2,2']

""")
        sleep(2)
        print("""Aqui está o corpo do nosso jogo, composto por 3 linhas e 3 colunas, como no papél, a seguir
digite a linha e a coluna relacionada a posição desejada. Você vai ser o X !
""")
        sleep(1)
        while True:
            linha = input('Escolha a linha: ')
            if linha.isnumeric():
                linha = int(linha)
                if linha in range(0, 3):
                    coluna = input('Escolha a coluna: ')
                    if coluna.isnumeric():
                        coluna = int(coluna)
                        if coluna in range(0, 3):
                            break
                        else:
                            print('Digite uma coluna válida !')
                    else:
                        print('Digite uma coluna válida! ')
                else:
                    print('Digite uma linha válida! ')
            else:
                print('Digite uma linha válida! ')
        print('')

        corpo[linha][coluna] = 'X'

        sleep(0.5)
        print('Sua Jogada:')
        for linha in range(0, 3):
            print(corpo[linha])

        sleep(1)
        jogador = 0



    else:
        print('\nEu começo! ')
        sleep(1)
        sleep(2)
        print("""Aqui está o corpo do nosso jogo, composto por 3 linhas e 3 colunas, como no papél, a seguir
digite a linha e a coluna relacionada a posição desejada. Você vai ser o X !
""")
        sleep(0.5)
        linha = randrange(0, 3)
        coluna = randrange(0, 3)

        corpo[linha][coluna] = 'O'

        print('Minha jogada: ')
        for linha in range(0, 3):
            print(corpo[linha])
        jogador = 1
        sleep(2)


def jogo(): #Desenvolver do Jogo

    global jogador
    global contador_velha
    while True:
        # -------------------------------------------Sistema de Vitória----------------------------------------------------------

        if corpo[0][0] == corpo[0][1] == corpo[0][2] and corpo[0][0] == corpo[0][1] == corpo[0][2] != '_':
            if corpo[0][0] == corpo[0][1] == corpo[0][2] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[1][0] == corpo[1][1] == corpo[1][2] and corpo[1][0] == corpo[1][1] == corpo[1][2] != '_':
            if corpo[0][0] == corpo[1][1] == corpo[1][2] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[2][0] == corpo[2][1] == corpo[2][2] and corpo[2][0] == corpo[2][1] == corpo[2][2] != '_':
            if corpo[2][0] == corpo[2][1] == corpo[2][2] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[0][0] == corpo[1][0] == corpo[2][0] and corpo[0][0] == corpo[1][0] == corpo[2][0] != '_':
            if corpo[0][0] == corpo[1][0] == corpo[2][0] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[0][1] == corpo[1][1] == corpo[2][1] and corpo[0][1] == corpo[1][1] == corpo[2][1] != '_':
            if corpo[0][1] == corpo[1][1] == corpo[2][1] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[0][2] == corpo[1][2] == corpo[2][2] and corpo[0][2] == corpo[1][2] == corpo[2][2] != '_':
            if corpo[0][2] == corpo[1][1] == corpo[2][2] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[0][0] == corpo[1][1] == corpo[2][2] and corpo[0][0] == corpo[1][1] == corpo[2][2] != '_':
            if corpo[0][0] == corpo[1][1] == corpo[2][2] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        elif corpo[0][2] == corpo[1][1] == corpo[2][0] and corpo[0][2] == corpo[1][1] == corpo[2][0] != '_':
            if corpo[0][2] == corpo[1][1] == corpo[2][0] == 'X':
                print('Você Ganhou !')
            else:
                print('Ganhei !')
            break
        # -------------------------------------------Sistema de Vitória----------------------------------------------------------

        if jogador == 0:
            sleep(0.5)
            print('Minha Vez ! \n')
            linha = randrange(0, 3)
            coluna = randrange(0, 3)
            while corpo[linha][coluna] != '_':
                linha = randrange(0, 3)
                coluna = randrange(0, 3)
            corpo[linha][coluna] = 'O'

            print('Minha jogada: \n')
            for linha in range(0, 3):
                print(corpo[linha])
            jogador = 1
            sleep(1)
        else:
            print('Sua Vez ! \n')
            sleep(0.5)
            print("""    linha, coluna
['0,0', '0,1', '0,2']
['1,0', '1,1', '1,2']
['2,0', '2,1', '2,2']

""")

            sleep(0.5)
            while True:
                linha = input('Escolha a linha: ')
                if linha.isnumeric():
                    linha = int(linha)
                    if linha in range(0, 3):
                        coluna = input('Escolha a coluna: ')
                        if coluna.isnumeric():
                            coluna = int(coluna)
                            if coluna in range(0, 3):
                                break
                            else:
                                print('Digite uma coluna válida !')
                        else:
                            print('Digite uma coluna válida! ')
                    else:
                        print('Digite uma linha válida! ')
                else:
                    print('Digite uma linha válida! ')
            print('')
            while corpo[linha][coluna] != '_':
                sleep(0.5)
                print('Escolha um lugar sem jogadas anteriores! \n')

                linha = int(input('Escolha a linha: '))
                coluna = int(input('Escolha a coluna: '))

            corpo[linha][coluna] = 'X'
            print('Sua jogada: \n')
            for linha in range(0, 3):
                print(corpo[linha])
            jogador = 0
            sleep(1)

        contador_velha += 1
        if contador_velha >= 9:
            print('\nDeu Velha !\n')
            break


bem_vindo()

jogo()
