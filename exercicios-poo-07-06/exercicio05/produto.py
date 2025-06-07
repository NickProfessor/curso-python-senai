class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome 
        self.__preco = preco 
        self.__estoque = estoque

    @property
    def mostrar_estoque(self):
        print(f'Estoque atual de {self.__nome}: {self.__estoque} unidades')

    def comprar(self, qtd):
        if qtd > self.__estoque:
            print('PRODUTO SEM ESTOQUE!!!')
        else:
            self.__estoque -= qtd
            print(f'Compra realizada de {qtd} unidades.')
        self.mostrar_estoque

    def repor(self, qtd):
        self.__estoque += qtd
        print(f'Estoque reposto com {qtd} unidades')
        self.mostrar_estoque


