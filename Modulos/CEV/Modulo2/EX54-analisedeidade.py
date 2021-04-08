from datetime import date
var = 0
contador = 0
cont = 0
atual = date.today().year
for ano in range(0,7):
    pessoa = ano + 1
    nas  = int(input('Digite o ano de nascimento da {}ª pessoa'.format(pessoa)))
    var = atual - nas

    if var < 18:
        contador = contador + 1
    else:
        cont = cont + 1
print('{} são menores e {} são maiores de idade!'.format(contador,cont))

