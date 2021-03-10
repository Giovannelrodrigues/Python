T1 = 0
T2 = 1

print('''======================
SEQUENCIA DE FIBONACCI
======================''')
num = int(input('Digite quantos termos você quer mostar'))
print('{}-->{}-->'.format(T1,T2), end='')
while num > 2:
     T3 = T1 + T2
     print('{}-->'.format(T3), end='')
     T1 = T2
     T2 = T3
     num -= 1
print('FIM')



