lista = []


for c in range(0,5):
    num = int(input('Digite um valor:'))

    if c == 0 or num > lista[len(lista)-1]:
        lista.append(num)
        print('Valor adcionado na ultima posição')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor inserido na posição {pos}')
                break
            pos += 1

print(f'Os valores inseridos foram {lista}')
     



