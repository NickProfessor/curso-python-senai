from produtos import Produto, ProdutoNacional, ProdutoImportado
from funcionarios import  FuncionarioCLT, FuncionarioPJ


produto_simples = Produto('Pão de forma', 7.5, 30)
print(f' Preço final produto simples R${produto_simples.preco_final()}')
produto_simples.emitir_nota()
produto_simples.vender(20)
produto_simples.exibir_detalhes()
print('====================================')

produto_nacional = ProdutoNacional('Leite', 6, 20)
produto_nacional.emitir_nota()
print('====================================')

produto_importado = ProdutoImportado("Celular", 2000.0, 5, 0.15)
print(f' Preço final produto importado R${produto_importado.preco_final()}')
produto_importado.emitir_nota()
produto_importado.vender(10)
produto_importado.vender(3)
produto_importado.exibir_detalhes()
print('====================================')


funcionarioCLT = FuncionarioCLT('João', 1510.00)
print(f'Salário CLT: R${funcionarioCLT.calcular_pagamento()}')

funcionarioPJ = FuncionarioPJ('Maria')
salarioPJ = funcionarioPJ.calcular_pagamento(120, 18)
print(f'Salário PJ: R${salarioPJ}')