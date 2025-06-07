class Carro:
    def __init__(self, modelo):
        self.__modelo = modelo
        self.__velocidade = 0

    @property
    def mostrar_velocidade(self):
        print(f'Velocidade atual: {self.__velocidade}Km/h')
    
    def acelerar(self):
        self.__velocidade += 10
        self.mostrar_velocidade

    def frear(self):
        if self.__velocidade - 10 < 0:
            self.__velocidade = 0
        else:
            self.__velocidade -= 10
        self.mostrar_velocidade