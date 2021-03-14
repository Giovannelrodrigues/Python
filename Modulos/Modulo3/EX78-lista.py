lista =[]
mm = 0
for cont in range(0,5):
    lista.append(int(input('Digite um número:')))

    #MaioreMenor

    maior = mm
    menor = mm
    for mm in lista:
        if mm > maior:
            maior = mm
        if mm < menor:
            menor = mm
#posição
for ind, c in enumerate(lista):
    if lista[ind] == maior:
        pmaior = ind
    if lista[ind] == menor:
        pmenor = ind
print('Numeros Digitados:',lista)
print(f'O maior número digitado foi {maior} e está na posição {pmaior}')
print(f'O menor número digitado foi {menor} e está na posição {pmenor}')
