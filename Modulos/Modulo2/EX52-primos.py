num = int(input('Digite um valor'))
tot = 0
for c in range(1,num +1):
    if num % c == 0:
        print('\033[33m',end = '')
        tot += 1
    else:
        print('\033[31m', end = '')
    print('{}'.format(c))
print('O número foi divisivel {} vezes'.format(tot))

if tot == 2:
    print('O número é primo!!')
else:
    print('O número não é primo')