#     Descrição:
# Um parque de diversões só permite que crianças maiores de 10 anos entrem em um brinquedo radical.
# Crie um programa que guarda a idade da criança numa variável e diga se ela pode ou não pode brincar.
# Entrada:  8
# Saída esperada: 
# A criança tem 8 anos  
# Você não pode entrar no brinquedo.
# Entrada:  12
# Saída esperada: 
# A criança tem 12 anos  
# Você pode entrar no brinquedo.
# Entrada:  10
# Saída esperada: 
# A criança tem 10 anos  
# Você não pode entrar no brinquedo.

idade = int(input('Informe a idade da criança: '))

print(f'A criança tem {idade} anos')
if idade < 10:
    print('Você não pode entrar no brinquedo')
else:
    print('Você pode entrar no brinquedo')