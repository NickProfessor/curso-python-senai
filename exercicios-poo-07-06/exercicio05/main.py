# 💵 Atividade 5 — Classe Produto
# Objetivo: Trabalhar com métodos que manipulam atributos numéricos.
# Crie uma classe Produto com:
# Atributos: nome, preco, estoque


# Métodos:


# comprar(qtd): reduz o estoque


# repor(qtd): aumenta o estoque


# mostrar_estoque(): imprime o estoque atual


# Garanta que o método comprar() não permita que o estoque fique negativo.

from produto import Produto

macarrao = Produto('Macarrão', 6, 20)

macarrao.comprar(5)
macarrao.repor(10)
macarrao.comprar(15)
macarrao.comprar(20)
macarrao.repor(20)
macarrao.comprar(30)