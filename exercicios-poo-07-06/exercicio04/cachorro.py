class Cachorro:
    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca
    
    @property
    def latir(self):
        print(f'AU AU! Meu nome é {self.__nome} e sou da raça {self.__raca}')