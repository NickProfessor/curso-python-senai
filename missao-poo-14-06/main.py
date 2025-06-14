from produto import Produto
from produto_nacional import ProdutoNacional
from produto_importado import ProdutoImportado

produto_simples = Produto('Pão de forma', 7.5, 30)
print(f' Preço final produto simples R${produto_simples.preco_final()}')
produto_simples.emitir_nota
produto_simples.vender(20)
produto_simples.exibir_detalhes
print('====================================')

produto_nacional = ProdutoNacional('Leite', 6, 20)
produto_nacional.emitir_nota
print('====================================')

produto_importado = ProdutoImportado("Celular", 2000.0, 5, 0.15)
print(f' Preço final produto importado R${produto_importado.preco_final()}')
produto_importado.emitir_nota
produto_importado.vender(10)
produto_importado.vender(3)
produto_importado.exibir_detalhes
print('====================================')
