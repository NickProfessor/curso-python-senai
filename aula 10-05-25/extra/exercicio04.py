# Atividade 4: Promoção progressiva
# Descrição:
#  Uma loja está com a seguinte promoção: se a compra for maior que R$ 200, ganha R$ 30 de desconto. Se for entre R$ 100 e R$ 200 (inclusive), ganha R$ 10 de desconto. Caso contrário, não ganha desconto.
#  Entrada: 250
#  Saída esperada:
#  Valor da compra: 250
#  Desconto de R$ 30 aplicado! Valor final: 220
#  Entrada: 150
#  Saída esperada:
#  Valor da compra: 150
#  Desconto de R$ 10 aplicado! Valor final: 140
#  Entrada: 80
#  Saída esperada:
#  Valor da compra: 80
#  Sem desconto aplicado. Valor final: 80

valor_compra = float(input('Insira o valor da compra: '))

if valor_compra > 200:
    valor_com_desconto = valor_compra - 30
    print(f'Desconto de R$ 30 aplicado! Valor final: {valor_com_desconto}')
elif valor_compra >= 100:
    
    valor_com_desconto = valor_compra - 10
    print(f'Desconto de R$ 10 aplicado! Valor final: {valor_com_desconto}')
else:
     print(f'Sem desconto aplicado. Valor final: {valor_compra}')