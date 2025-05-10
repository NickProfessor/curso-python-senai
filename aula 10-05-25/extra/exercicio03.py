# Atividade 3: Pode dirigir?
# Descrição:
#  Crie um programa que guarda a idade de uma pessoa e diga se ela já pode tirar carteira de motorista (a partir dos 18 anos).
#  Entrada: 17
#  Saída esperada:
#  Idade: 17
#  Você ainda não pode tirar carteira de motorista.
#  Entrada: 20
#  Saída esperada:
#  Idade: 20
#  Você já pode tirar carteira de motorista!

idade = int(input('Insira sua idade: '))

print(f'Idade: {idade}')
if idade >= 18:
    print('Você já pode tirar carteira de motorista!')
else:
    print('Você ainda não pode tirar carteira de motorista.')