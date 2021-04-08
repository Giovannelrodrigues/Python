num = int(input('Digite o valor para calcular fatorial'))
c = num
soma = 1

while c > 0:

    soma *= c

    print(c,end='')
    if c > 1:
        print(' X ', end='')
    else:
        print(' = ', end='')
    c-= 1

print(soma, end='')
