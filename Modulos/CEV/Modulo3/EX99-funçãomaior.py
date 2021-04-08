continuar = 1
ma = menor = 0
lista = []
def linha():
    print('~' * 30)

def maior(*num):
    ma = 0
    linha()
    for c in lista:
        if c > ma:
            ma = c
    print(f'Valores digitados {lista} e o maior é {ma}')
    linha()
        

while continuar != 0:
    continuar = int(input('Digite um valor, [0]Encerra:'))
    if continuar != 0:
        lista.append(continuar)

maior(lista)