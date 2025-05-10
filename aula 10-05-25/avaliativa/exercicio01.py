# Atividade 1 – Algoritmo com tomada de decisão (lógica básica)
# Descrição:
# Crie um algoritmo (pode ser uma narrativa ou fluxograma) que simule uma máquina de refrigerante:
# O usuário deve escolher entre 3 opções de bebida


# A máquina deve entregar a bebida escolhida ou informar se a opção é inválida


# Objetivos avaliados:
# Algoritmo simples com decisão


# Clareza na lógica



lista_refrigerantes = ['Coca-Cola light', 'Coca-cola normal', 'Coca-cola zero']

    
resposta = ''
print('\n\n')
print('Veja nossas opções de refris!')
print('\n\n')
while resposta == '' or not (0 < resposta < 4)  :
    if resposta != '':
        print('\n\n')
        print('Opção inválida. Opções disponíveis: 1, 2, 3')
        print('\n\n')
    for idx, refri in enumerate(lista_refrigerantes):
        print(f'{idx + 1} - {refri}')
    try:
        print('\n\n')
        resposta = int(input('Informe qual refri você vai querer! Digite o número referente ao produto: '))
        print('\n\n')
    except ValueError:
        print('\n\n')
        print(f'Você deve informar um número entre 1, 2 ou 3!')
        print('\n\n')
        resposta = ''   
     
print(f'Opção escolhida foi {lista_refrigerantes[0]}')