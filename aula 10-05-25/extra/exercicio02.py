# Atividade 2: Nota para passar
# Descrição:
#  Um aluno precisa tirar pelo menos 7 para ser aprovado. Crie um programa que guarda a nota em uma variável e diga se ele foi aprovado ou reprovado.
#  Entrada: 6.5
#  Saída esperada:
#  Nota: 6.5
#  Reprovado.
#  Entrada: 8.2
#  Saída esperada:
#  Nota: 8.2
#  Aprovado!

nota = float(input('Insira a nota de um aluno: '))
print(f'Nota: {nota}')
if nota >= 7:
    print('Aprovado')
else:
    print('Reprovado')
    