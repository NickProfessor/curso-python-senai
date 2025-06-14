# Atividade 1 – Criando a classe base Produto
# Conceitos: Classe, atributos, métodos, __init__
# Crie a classe Produto com os seguintes atributos:
# nome


# preco


# estoque


# Adicione um método exibir_detalhes() que imprima:
#  Produto: nome | Preço: R$preco | Estoque: X unidades

class Produto:
    def __init__(self, nome, preco, estoque):
        self._nome = nome
        self._preco = preco
        self._estoque = estoque

    
    def exibir_detalhes(self):
        print(f'Nome do produto: {self._nome}')
        print(f'Valor: R${self._preco}')
        print(f'Estoque: {self._estoque} unidades')

    def preco_final(self):
        return self._preco

    
    def emitir_nota(self):
        print(f'Nota gerada para {self._nome}')

    def repor(self, quantidade):
        self._estoque += quantidade
        print(f'Foram adicionadas {quantidade} unidades de {self._nome}. Estoque atual: {self._estoque}')

    def vender(self, quantidade):
        if quantidade > self._estoque:
            print('Impossível finalizar compra. Ñão há estoque disponível')
        else:
            self._estoque -= quantidade
            print(f'Compra realizada no valor de R${self._preco * quantidade}. ')