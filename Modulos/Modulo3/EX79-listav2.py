lista = []
continuar = 'S'


while continuar == 'S':
    num = (int(input('Digite um valor:')))
    if num not in lista:
        lista.append(num)
    else:
        num = (int(input('Este número ja foi digitado, tente outro:')))

    continuar = str(input('Deseja continuar?[S/N]:')).strip().upper()[0]
    lista.sort()
print(f'Os valores digitados em ordem crescente é {lista}')