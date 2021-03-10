contador = soma = 0

while True:
    n = int(input('Digite um valor a ser somado:'))
    if n !=0:
        contador += 1
        soma += n
    if n == 0:
        break
print(f'A soma dos valores digitados é de {soma}')
print(f'{contador} números foram digitados')