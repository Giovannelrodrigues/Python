class Erro(Exception):
    pass

class InputErro(Erro):
    def __init__(self, menssage):
        self.menssage = menssage


while True:
    try:
        num = int(input('Digite uma nota de [0 a 10]: '))
        if num > 10 or num < 0:
            raise InputErro('''Nota não pode ser inserida!
Nota não pode ser menor que 0
Nota não pode ser maior que 10
==============================''')
        break
    except ValueError:
        print('Valor Inválido! Apenas Números')
    except InputErro as ex:
        print(ex)

