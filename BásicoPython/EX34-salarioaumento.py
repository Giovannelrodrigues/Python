sal = float(input('Digite o valor do seu sálario'))

if sal < 1250:
    salau = sal / 100 * 10 + sal
    des = 10
else:
    salau = sal / 100 * 15 + sal
    des = 15

print('O valor do sálario com aumento é de {}'.format(salau))
print('O valor do aumento aplicado foi de {}%'.format(des))