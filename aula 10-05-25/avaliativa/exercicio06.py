# Calculadora de operações básicas (menu interativo)
# Descrição:
#  Monte um menu com as opções:
# 1 - Somar  
# 2 - Subtrair  
# 3 - Multiplicar  
# 4 - Dividir  
# 5 - Sair

# O programa deve pedir dois números e aplicar a operação escolhida.


# Repetir o menu até o usuário escolher "Sair".


# Objetivos avaliados:
# Laço while


# Condicionais múltiplas


# Operadores aritméticos

try:
    resposta = ''
    while resposta != '5':
        print('''
            1 - Somar  
            2 - Subtrair  
            3 - Multiplicar  
            4 - Dividir  
            5 - Sair
              ''')
        resposta = input('Escolha uma opção!: ')
        if resposta != '5' and int(resposta) < 5:
            numero1 = float(input('Insira um número: '))
            numero2 = float(input('Insira outro valor: '))
        if resposta == '1':
            print(f'Resultado da soma: {numero1 + numero2}')
        if resposta == '2':
            print(f'Resultado da subtração: {numero1 - numero2}')
        if resposta == '3':
            print(f'Resultado da multiplicação: {numero1 * numero2}')
        if resposta == '4':
            print(f'Resultado da divisão: {numero1 / numero2}')
except (ValueError, ZeroDivisionError):
    print('Você fez caca')