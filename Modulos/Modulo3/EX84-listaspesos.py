listaGeral = []
listaDosIndividuos = []
listaDeMaiorPeso = []
listaDeMenorPeso = []
continuar = 'S'
maior = menor = 0


while continuar == 'S':
    listaDosIndividuos.append(str(input('Digite seu nome:')))
    listaDosIndividuos.append(float(input('Digite seu peso:')))
    
    if len(listaGeral) == 0:
        maior = menor = listaDosIndividuos[1]
    else:
         if listaDosIndividuos[1] > maior:
             maior = listaDosIndividuos[1]
         if listaDosIndividuos[1] < menor:
             menor = listaDosIndividuos[1]

    listaGeral.append(listaDosIndividuos[:])
    listaDosIndividuos.clear()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

for pessoa in listaGeral:
    if pessoa[1] == maior:
        listaDeMaiorPeso.append(pessoa[0])
    if pessoa[1] == menor:
        listaDeMenorPeso.append(pessoa[0])
print('=' * 40)
print(f'{len(listaGeral)} FORAM REGISTRADAS!')
print('=' * 40)
print(f'O maior peso é de{maior}k/g. Peso de {listaDeMaiorPeso}')
print(f'O menor peso é de{menor}k/g. peso de {listaDeMenorPeso}')
print('=' * 40)


