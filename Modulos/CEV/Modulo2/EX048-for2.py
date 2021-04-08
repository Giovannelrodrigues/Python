soma = 0
cont = 0
for conta in range(1,500):
    if conta % 3 ==0:
        soma += conta
        cont = cont + 1
print('Resultado = {}\nQuantidade de números somados {}'.format(soma,cont))