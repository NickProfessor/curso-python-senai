# Repetição com while até acertar a senha
# Crie um programa que:
# Defina uma senha numérica (ex: 3003)
# Enquanto a senha estiver incorreta, continue deixando o usuário adivinhar com dicas: “Maior” ou “Menor”
# Quando for correta, exibe “Acesso permitido”

senha = 2201

palpite = ''

try:
    while palpite != senha:
        print('Tente acertar a senha')
        if palpite != '':
            if palpite > senha:
                print(f'O número secreto é menor que {palpite}')
            else:
                print(f'O número secreto é maior que {palpite}')
            palpite = int(input('Insira outro palpite: '))
        else:
            palpite = int(input('Faça seu palpite: '))
            
    print('VOCE ACERTOUUUU')
except ValueError:
    print('SOMENTE NÚMEROS')