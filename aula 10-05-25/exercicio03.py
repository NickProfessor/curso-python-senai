# Atividade 3: Comprando com desconto
# Descrição:
# Você tem uma variável com o valor de uma compra. Se o valor for maior que R$ 100, o cliente ganha 10 reais de desconto.
# Mostre o valor final a pagar com ou sem o desconto.
# Entrada:  120
# Saída esperada:
# Valor da compra: 120  
# Desconto aplicado! Valor final: 110
# Entrada:  100
# Saída esperada:
# Valor da compra: 100  
# Sem desconto aplicado! Valor final: 100
# Entrada:  80
# Saída esperada:
# Valor da compra: 80  
# Sem desconto aplicado! Valor final: 80

valor_compra = float(input('Informe o valor da compra: '))

print(f'Valor da compra: {valor_compra}')
if valor_compra > 100:
    valor_com_desconto = valor_compra - 10
    print(f'Desconto aplicado! Valor final: {valor_com_desconto}')
else:
    print(f'Sem desconto aplicado! Valor final: {valor_compra}')