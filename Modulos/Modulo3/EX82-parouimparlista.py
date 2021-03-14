lpar = []
limpar = []
lsoma = []

continuar = 'S'
while continuar == 'S':
    num = int(input('Digite um valor'))
    lsoma.append(num)

    if num % 2 == 0:
        lpar.append(num)
    else:
        limpar.append(num)

    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
print('='*40)
print(f'Todos os valores digitados: {lsoma}')
print(f'Todos os valores par digitados: {lpar}')
print(f'Todos os valores impar digitados: {limpar}')
print('='*40)
