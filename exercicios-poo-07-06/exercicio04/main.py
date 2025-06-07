# 🐶 Atividade 4 — Classe Cachorro
# Objetivo: Trabalhar com métodos simples e múltiplas instâncias.
# Crie a classe Cachorro com:
# Atributos: nome, raca


# Método latir() que imprime:
#  "Au au! Eu sou o NOME, da raça RAÇA."


# Crie pelo menos 3 cachorros e chame latir() para cada um.

from cachorro import Cachorro

dog1 = Cachorro('Stitch', 'Alien')
dog2 = Cachorro('Bolt', 'Super-Cão')
dog3 = Cachorro('Caramelo', 'Caramelo')

dog1.latir
dog2.latir
dog3.latir