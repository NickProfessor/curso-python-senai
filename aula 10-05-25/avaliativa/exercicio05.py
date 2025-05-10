#     Descrição:
#  Faça um programa que:
# Peça um número ao usuário


# Informe se é par ou ímpar


# Pergunte se o usuário deseja testar outro número (S/N)


# Só encerra se o usuário digitar N


# Objetivos avaliados:
# Uso de while com controle condicional


# Lógica e reutilização

try:
    resposta = 'SIM'
    while resposta == 'SIM':
        numero = int(input('Insira um número inteiro: '))
        if numero % 2 == 0:
            print(f'Número {numero} é par')
        else:
            print(f'Número {numero} é ímpar')
        resposta = input('Deseja tentar um novo número? Digite SIM: ').upper()
    print('Obrigado!')
except ValueError:
    print('SÓ UTILIZE NUMEROS INTEIROS')