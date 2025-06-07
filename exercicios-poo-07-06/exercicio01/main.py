# 📝 Atividade 1 — Classe Pessoa
# Objetivo: Criar atributos e um método simples.
# Crie uma classe Pessoa com os seguintes atributos:
# nome
# idade
# E um método apresentar() que imprime:
# "Olá, meu nome é NOME e tenho IDADE anos."
# Crie duas pessoas diferentes e chame o método apresentar() para cada uma.


from pessoa import Pessoa

joao = Pessoa('João Pedro', 18)
maria = Pessoa('Maria Joaquina', 20, 'Analista de Sistemas')

joao.apresentar
maria.apresentar