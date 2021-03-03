soma = 0
for cont in range(0,5):
    var = int(input('Digite um valor'))
    if var % 2 == 0:
        soma += var
print('O resultado é: {}'.format(soma))
