# Atividade 2: Par ou ímpar?
# Descrição:
# Crie um programa que guarda um número numa variável e diz se ele é par ou ímpar.
# Dica: use o operador % para descobrir o resto da divisão por 2.
# Entrada:  12
# Saída esperada: O número 12 é par.
# Entrada:  7
# Saída esperada: O número 7 é ímpar.

numero = int(input('Informe um número inteiro: '))

if numero % 2 == 0:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')

