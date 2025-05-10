# Atividade 4 – Laço for: contagem regressiva com passo
# Descrição:
#  Peça ao usuário um número inicial e final, e imprima a contagem regressiva de 2 em 2 até 0 (ou o final indicado).
# Exemplo de saída:
# Digite o início: 10  
# Digite o fim: 0  
# 10 8 6 4 2 0

# Objetivos avaliados:
# Uso de range(inicio, fim, passo)


# Controle de repetição com for

try:
    inicio = int(input('Insira o começo da contagem: '))
    final = int(input('Insira o final da sua contagem: '))
    
    if inicio < final:
        for numero_atual in range (inicio, final +1, 2):
            print(numero_atual)
    elif final < inicio:
        for numero_atual in range (inicio, final -1, -2):
            print(numero_atual)
    else:
        print('Os dois números são iguais. Impossível realizar contagem')
except ValueError:
    print('SO INSIRA NUMEROS INTEIROS')