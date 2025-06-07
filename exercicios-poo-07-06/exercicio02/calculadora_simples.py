class CalculadoraSimples:
    def somar(a, b):
        print(f'A soma de {a} com {b} resultou em: {a+b}')
    def subtrair(a, b):
        print(f'A subtração de {a} com {b} resultou em: {a-b}')
    def multiplicação(a, b):
        print(f'A multiplicação de {a} com {b} resultou em: {a*b}')
    def dividir(a, b):
        try:
            print(f'A divisão de {a} com {b} resultou em: {a/b}')
        except ZeroDivisionError:
            print(f'A divisão de {a} com {b} não é possível pois o divisor não pode ser 0')