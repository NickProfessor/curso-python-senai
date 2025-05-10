#  Atividade 2 – Classificador de número (condicional)
# Descrição:
# Escreva um programa em Python que leia um número inteiro e classifique-o como:
# Positivo


# Negativo


# Zero


# Objetivos avaliados:
# Uso de if, elif, else


# Estrutura básica de entrada/saída

try:
    numero = float(input('Insira um número qualquer: '))
    if numero > 0:
        print('Número positivo')
    elif numero < 0:
        print('Número negativo')
    else:
        print('Número zero')
except ValueError:
    print('Valor inserido não é válido', 'Use números!', sep='\n')