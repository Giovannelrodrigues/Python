
menor = 0
maior = 0
for first in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa:'.format(first)))
    if first == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {}Kg, e o menor é {}Kg.'.format(maior, menor))