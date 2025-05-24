# Exercício 3: Cálculo de frete
# Enunciado:
#  Crie uma função que receba o peso de uma encomenda e retorne o valor do frete:
# Até 1kg: R$ 10


# Até 5kg: R$ 20


# Acima de 5kg: R$ 30

def calcular_frete(peso):
    if peso <= 1000:
        return 10.00
    elif peso <= 5000:
        return 20.00
    else:
        return 30.00
    
peso = float(input('Insira o peso da compra em GRAMAS: '))

frete = calcular_frete(peso)

print(f'O frete a ser pago será de R${frete}')