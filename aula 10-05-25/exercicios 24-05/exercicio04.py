# Exercício 4: Conversor de notas para conceito
# Enunciado:
#  Crie uma função que converta uma nota de 0 a 100 para conceitos:
# A (90–100), B (80–89), C (70–79), D (60–69), F (0–59)

def converte_nota(valor):
    if valor >= 90:
        return 'A'
    if valor >= 80:
        return 'B'
    if valor >= 70:
        return 'C'
    if valor >= 60:
        return 'D'
    return 'F'

nota_em_numero = float(input('Informe o número: '))
if nota_em_numero > 100 or nota_em_numero < 0:
    print('Nota inválida. Informe uma nota de 0 a 100')
else:
    nota = converte_nota(nota_em_numero)
    print(f'Nota: {nota}')