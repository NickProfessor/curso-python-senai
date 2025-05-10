# Monte um programa com este menu dentro de um while:
# MENU
# 1 - Converter Celsius para Fahrenheit ((C * 1,8) + 32.)
# 2 - Calcular idade (ano nascimento)
# 3 - Sair

# Se a pessoa digitar 1, pedir a temperatura e converter
# Se digitar 2, pedir ano de nascimento e calcular idade
# Se digitar 3, encerrar com uma mensagem de “Até logo!”



resposta = ''

try:
    while resposta != '3':
        print('''
        1. Converter Celsius para Fahrenheit
        2. Calcular idade
        3. Sair
        ''')
        
        resposta = input('Escolha uma opção: ')
            
        if resposta == '1':
            celsius = float(input('Insira a temperatura em celsius (somente o número): '))
            fahrenheit = celsius * 1.8 +32
            print(f'Temperatura: {fahrenheit}ºF')
        elif resposta == '2':
            ano_nasc = float(input('Insira seu ano de nascimento: '))
            idade = 2025 - ano_nasc
            print(f'Idade: {idade} anos')
        elif resposta == '3':
            print('Saindo...')
        else:
            print('Opção inválida')
except ValueError:
    print('TRABALHE COM NÚMEROS')