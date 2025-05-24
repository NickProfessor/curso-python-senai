# Exercício 1: Validação de senha
# Enunciado:
# Peça ao usuário uma senha e valide se ela contém pelo menos 8 caracteres, uma letra maiúscula e um número.



def valida_senha(senha):
    for letra in senha:
        if letra.isnumeric:
            tem_numero = True
        if letra.isupper():
            tem_maiusculo = True
    if len(senha) >= 8 and tem_numero and tem_maiusculo:
        return True
    else:
        return False
    
senha = input('Crie uma senha:')
validada = valida_senha(senha)
if validada:
    print('Sucesso ao criar senha!')
else:
    print('Falha ao criar senha. Sua senha dever conter pelo menos 8 caracteres, uma letra maiúscula e um número.')
  