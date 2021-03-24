listaPar = []
listaImpar = []

continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um número:'))

    if num % 2 == 0:
        listaPar.append(num)
        print(listaPar)
    if num % 2 == 1:
        listaImpar.append(num)
        print(listaImpar) 

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

listaPar.sort()
listaImpar.sort()

print('=' * 40)
print(f'Números pares digitados:{listaPar}')
print(f'Números impares digitados:{listaImpar}')
print('=' * 40)