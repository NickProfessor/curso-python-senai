# Exercício 6: Gerador de e-mails institucionais
# Enunciado:
# Dado o nome completo do aluno, gere um e-mail no formato primeironome.sobrenome@escola.com.

def gera_email(nome):
    for letra in nome:
        if letra == '@':
            print('Email não é possível de ser criado')
            exit()
    nome = nome.lower()
    nomes = nome.split(' ')
    primeiro_nome = nomes[0]
    segundo_nome = nomes[1]
    return f'{primeiro_nome}.{segundo_nome}@escola.com'

nome = input('Informe seu nome: ')
email = gera_email(nome)

print(f'Email institucional: {email}')