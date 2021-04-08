numeros = (int(input('Digite um valor:')), 
int(input('Digite um valor:')), 
int(input('Digite um valor:')), 
int(input('Digite um valor:')))

print(numeros.count(9),'numeros 9 foram encontrados')
print('número 3 foi encontrado na posição:', numeros.index(3))

for cont in range(0, len(numeros)):
    if numeros[cont] % 2 == 0:
        print('Numeros Pares:',numeros[cont], '-->', end='')
