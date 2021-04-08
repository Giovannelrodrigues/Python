from random import randint

cont = soma = 0
listaNum = []

def linha():
    print('~' * 30)

def sorteio(listaNum):
    linha()
    for c in listaNum:
        print(c, '-->',end='')
    print('FIM')
def soma(listaNum):
    soma = 0
    for c in listaNum:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos pares desta lista é de {soma}')
    linha()


quant = (int(input('Digite quantos a ser sorteado:')))

while cont < quant:
    listaNum.append(randint(1,10))
    cont += 1

sorteio(listaNum)
soma(listaNum)