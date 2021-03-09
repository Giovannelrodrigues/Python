pr = int(input('Qual o primero termo da pa?'))
ra = int(input('Qual a razão da pa?'))
ter = pr
c = 0

while c <= 10:
    print('{} --> '.format(ter), end='')
    ter += ra
    c += 1
print('FIM')