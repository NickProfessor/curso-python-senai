# Exercício 8: Jogo de par ou ímpar
# Enunciado:
# Faça um jogo entre o usuário e o computador (número entre 0 e 10). O usuário escolhe par ou ímpar e o número. Quem vencer?
# dica: use a função random

import random
print('IMPÁR OU PAR??')

escolha = input('Escolha uma opção: 1-IMPAR 2-PAR \n')
numero = int(input('Fale um número de 0 a 10: '))
numero_aleatorio = int(random.random() * 10)
soma = numero + numero_aleatorio
print(f'{numero_aleatorio} foi o número escolhido pelo computador')

def exibeVencedor(jogador, computador):
    if escolha == 2 and soma % 2 == 0:
        print('JOGADOR VENCEU!!')
    elif escolha == 1 and soma % 2 != 0:
        print('JOGADOR VENCEU')
    elif escolha == 2 and soma % 2 != 0:
        print('JOGADOR PERDEU!!')
    else:
        print('JOGADOR PERDEU')
    exit()

exibeVencedor(numero, numero_aleatorio)