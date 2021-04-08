class Calculadora:
    def __init__(self):
        pass
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

Calculadora = Calculadora()

print(Calculadora.soma(10,2))
print(Calculadora.subtracao(5,3))
print(Calculadora.multiplicacao(100,2))
print(Calculadora.divisao(10,5))