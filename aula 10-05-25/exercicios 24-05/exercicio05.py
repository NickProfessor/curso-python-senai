# Exercício 5: Estatísticas de uma lista
# Enunciado:
#  Receba uma lista de números do usuário. Crie funções para retornar a média, o maior e o menor número.

parar = ''
lista = []
while parar.upper() != 'SIM':
    numero = int(input('\nInsira um número na lista: \n'))
    lista.append(numero)
    parar = input('\nDeseja parar de inserir números? Se não, vamos pedir mais um número: \n')


def calcularMedia(lista):
    soma = 0
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    return media

def pega_maior(lista):
    numero_anterior = 0
    for numero in lista:
        if numero == lista[0]:
            maior = numero
        else:
            if numero >= numero_anterior:
                maior = numero
        numero_anterior = numero
    return maior


def pega_menor(lista):
    numero_anterior = 0
    for numero in lista:
        if numero == lista[0]:
            menor = numero
        else:
            if numero <= numero_anterior:
                menor = numero
        numero_anterior = numero
    return menor

media, maior, menor = calcularMedia(lista), pega_maior(lista), pega_menor(lista)

print(f'\n\nMédia: {round(media, 2)}')
print(f'Maior número: {maior}')
print(f'Menor: {menor}')