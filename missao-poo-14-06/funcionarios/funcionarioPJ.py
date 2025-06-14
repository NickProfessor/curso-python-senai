from .funcionario import Funcionario

class FuncionarioPJ(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)

    def calcular_pagamento(self, horas_trabalhadas, valor_hora):
        return horas_trabalhadas * valor_hora