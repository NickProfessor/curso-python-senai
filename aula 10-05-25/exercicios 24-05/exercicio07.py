# Exercício 7: Simulador de caixa eletrônico
# Enunciado:
#  Peça um valor e informe quantas notas de R$100, R$50, R$20, R$10 e R$2 são necessárias para compor o valor.

def calcular_notas(valor):
    notas = 0
    
    notas += valor // 100
    notas_cem = valor // 100
    valor -= 100 * (valor // 100)

    notas += valor // 50
    notas_cinquenta = valor // 50
    valor -= 50 * (valor // 50)

    notas += valor // 20
    notas_vinte = valor // 20 
    valor -= 20 * (valor // 20)

    notas += valor // 10
    notas_dez = valor // 10
    valor -= 10 * (valor // 10)

    notas += valor // 2
    notas_dois = valor // 2
    valor -= 2 * (valor // 2)

    if valor != 0:
        print('Valor não é possível para saque')
        exit()
    else:
        return {
            'notas': notas,
            'notas_cem': notas_cem,
            'notas_cinquenta': notas_cinquenta,
            'notas_vinte': notas_vinte,
            'notas_dez': notas_dez,
            'notas_dois': notas_dois
        }
    
valor = int(input('Informe quanto você quer sacar? (NOTAS DISPONÌVEIS: R$100, R$50, R$20, R$10 e R$2)'))
notas = calcular_notas(valor)

print(f'''
    Notas de cem: {notas['notas_cem']}
    Notas de cinquenta: {notas['notas_cinquenta']}
    Notas de vinte: {notas['notas_vinte']}
    Notas de dez: {notas['notas_dez']}
    Notas de dois: {notas['notas_dois']}
    -----------------
    Notas no geral: {notas['notas']}
      ''')