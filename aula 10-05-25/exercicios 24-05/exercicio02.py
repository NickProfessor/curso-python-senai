# Exercício 2: Contagem regressiva com atraso
# Enunciado:
#  Crie uma função que faça uma contagem regressiva a partir de um número dado, com 1 segundo de intervalo entre os números.
# dica: use a lib time

import time



def contagem_regressiva(numero):
    for i in range(numero, -1, -1):
        time.sleep(1)
        print(i)

numero_dado = int(input('Informe o começo da contagem regressiva: '))
contagem_regressiva(numero_dado)