from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome):
        self._nome = nome
    
    @abstractmethod
    def calcular_pagamento(self):
        pass