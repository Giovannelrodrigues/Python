materiais = 'Borracha', 2, 'Tessoura', 10, 'caderno', 40, 'estojo', 25, 'Lápis', 0.75, 'Mochila', 150 

print('-' * 40)
print(f'{"Lista de Materiais":^40}')
print('-' * 40)


for po in range(0, len(materiais)):
    if po % 2 ==0:
        print(f'{materiais[po]:.<30}', end='')
    else:
        print(f'R${materiais[po]:>7.2f}')
print('-' * 40)