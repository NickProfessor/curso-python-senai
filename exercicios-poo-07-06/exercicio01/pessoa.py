class Pessoa:
    def __init__(self, nome, idade, profissao='desempregado'):
        self.__nome = nome
        self.__idade = idade
        self.__profissao = profissao

    @property
    def apresentar(self):
        print(f'Prazer, sou o {self.__nome}, tenho {self.__idade} anos. Atualmente atuo como {self.__profissao}')
