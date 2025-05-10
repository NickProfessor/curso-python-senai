# Tabuada com for
# Solicite um número e exiba sua tabuada de 1 a 10.
# Entrada: 5
# Saída esperada: 
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50

try:
    numero = int(input('Insira um número: '))
    for numero_atual in range(1, 11):
        resultado = numero_atual * numero
        print(f'{numero} x {numero_atual} = {resultado}')
except ValueError:
    print('SOMENTE NÚMEROS')