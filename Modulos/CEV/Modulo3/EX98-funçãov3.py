from time import sleep

def contar(inicio, fim, passo):
    for c in range(1,11):
        print(c,)
        sleep(0.5)
    print('FIM')
    for c in range(10,0,-2):
        print(c)
        sleep(0.5)
    print('FIM')
    for c in range(inicio, fim, passo):
        print(c)
        sleep(0.5)
    print('FIM')

inicio = int(input('Digite o inicio:'))
fim = int(input('Digite o fim:'))
passo = int(input('Digite de quantos vai pular'))

contar(inicio, fim, passo)
