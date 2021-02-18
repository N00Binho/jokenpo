# Crie um programa que faça ele jogar JOKENPÔ com você

import random
from time import sleep

while True:
    representacao = random.randint(0, 2)

    sua_jogada = str(input('Escreva Pedra, Papel ou Tesoura (-1 encerra aplicação)\n')).strip().lower()

    if representacao == 0:
        jogada_da_maquina = 'pedra'
    elif representacao == 1:
        jogada_da_maquina = 'papel'
    elif representacao == 2:
        jogada_da_maquina = 'tesoura'
    else:
        jogada_da_maquina = False

    if sua_jogada == '-1':
        print('--Obrigado por Jogar--')
        break

    print('JO', end='')
    sleep(0.5)
    print('KEN', end='')
    sleep(0.5)
    print('PÔ')

    print('-='*11)

    if jogada_da_maquina == sua_jogada:
        print('Empate')
    elif jogada_da_maquina == 'pedra' and sua_jogada == 'tesoura':  # Máquina jogou pedra e jogador tesoura
        print('Máquina Venceu')
    elif jogada_da_maquina == 'tesoura' and sua_jogada == 'pedra':  # Máquina jogou tesoura e jogador pedra
        print('Player Venceu')
    elif jogada_da_maquina == 'papel' and sua_jogada == 'tesoura':  # Máquina jogou papel e jogador jogou tesoura
        print('Player Venceu')
    elif jogada_da_maquina == 'tesoura' and sua_jogada == 'papel':  # Máquina jogou tesoura e jogador jogou papel
        print('Máquina Venceu')
    elif jogada_da_maquina == 'pedra' and sua_jogada == 'papel':  # Máquina jogou pedra e jogador jogou papel
        print('Player Venceu')
    elif jogada_da_maquina == 'papel' and sua_jogada == 'pedra':  # Máquina jogou papel e jogador jogou pedra
        print('Máquina Venceu')
    elif sua_jogada != 'pedra' or sua_jogada != 'papel' or sua_jogada != 'tesoura':  # O jogador não jogou direito
        print('Você não inseriu um valor válido')

    print('A máquina jogou {} e o jogador jogou {}'.format(jogada_da_maquina, sua_jogada))

    print('-='*11)

