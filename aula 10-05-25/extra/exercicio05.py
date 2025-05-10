# Atividade 5: Classificação de filmes
# Descrição:
#  Crie um programa que recebe a classificação indicativa de um filme (idade mínima recomendada) e a idade do espectador, e diga se ele pode assistir ao filme ou não.
#  Entrada:
#  Classificação indicativa: 16
#  Idade do espectador: 14
#  Saída esperada:
#  Classificação: 16 anos
#  Sua idade: 14
#  Você não pode assistir a este filme.
#  Entrada:
#  Classificação indicativa: 12
#  Idade do espectador: 13
#  Saída esperada:
#  Classificação: 12 anos
#  Sua idade: 13
#  Você pode assistir a este filme!

idade_indicada = int(input('Insira a classificação indicativa de um filme (idade mínima recomendada): '))
idade = int(input('Insira a sua idade: '))

print(f'Classficiação: {idade_indicada} anos')
print(f'Sua idade: {idade}')
if idade >= idade_indicada:
    print('Você pode assistir a este filme!')
else:
    print('Você não pode assistir a este filme.')