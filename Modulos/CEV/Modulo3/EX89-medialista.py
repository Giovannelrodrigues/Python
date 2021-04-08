listaNomeMedia = []
listaDados = []
listaNotaP = []
listaNotas = []
listaLista = []
contador = num1 = num2 = c = 0
continuar = 'S'

while continuar == 'S':   
    listaDados.append(str(input('Nome:')))
    num1 = int(input('Digite a primeira nota:'))
    num2 = int(input('Digite a segunda nota'))
    listaNotaP.append(num1)
    listaNotaP.append(num2)
    soma = (num1 + num2) / 2
    listaDados.append(soma)
    listaNomeMedia.append(listaDados[:])
    listaNotas.append(listaNotaP[:])
    listaNotaP.clear()
    listaDados.clear()
    contador +=1
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

for cont in listaNomeMedia:
    print(f'{c}    {cont[0]}   {cont[1]}')
    c += 1

mostrar = int(input('Digite número correspondente para mostrar notas:'))
listaLista.append(listaNotas)
for m in listaLista:
    print(f'1ª nota:{m[1][mostrar]}  2ªnota{m[1][mostrar]}')


