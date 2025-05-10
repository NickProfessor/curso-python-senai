# Descrição:
#  Crie um programa que guarda a temperatura atual em uma variável e verifica se ela está dentro da faixa ideal para nadar (entre 25 e 30 graus, inclusive).
#  Entrada: 27
#  Saída esperada:
#  Temperatura: 27°C
#  Está ideal para nadar!
#  Entrada: 22
#  Saída esperada:
#  Temperatura: 22°C
#  Muito frio para nadar.

temperatura_atual = float(input('Insira a temperatura atual: '))

print(f'Temperatura: {temperatura_atual}ºC')
if 25 <= temperatura_atual <= 30:
    print('Está ideal pra nadar!')
else:
    print('Muito frio para nadar!')