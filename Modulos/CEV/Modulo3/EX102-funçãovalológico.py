def fatorial(num, boole):
    soma = 1
    print('~' * (n * 5 + 1))
    for c in range(n, 0, -1):
        if tf == 'True':
            print(c, end='')
            if boole == 'True':
                print(' X ', end='')  
            if c == 1:
                print(' = ', end='')
        soma *= c

    if tf == 'False':
        print(f'A respota é {soma}')

    print('~' * (n * 5 + 1))

n = int(input('Valor da para calcular fatorial:'))
tf = str(input('Digite True or False:')).strip().title()

fatorial(n,tf)
