from produto import Produto

class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.__taxa_importacao = taxa_importacao

    @property
    def exibir_detalhes(self):
        super().exibir_detalhes
        print(f'Taxa de importação', self.__taxa_importacao)

    def preco_final(self):
        return self._preco + (self.__taxa_importacao * self._preco)
    
    @property
    def emitir_nota(self):
        print(f'Nota de importação para {self._nome} com taxa aplicada')
    
    def vender(self, quantidade):
        if quantidade > self._estoque:
            print('Impossível realizar compra.')
        else:
            self._estoque -= quantidade
            print(f'Compra realizada no valor de R${self.preco_final() * quantidade}')