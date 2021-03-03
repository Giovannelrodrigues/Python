pre = float(input('Digite o valor do produto em R$'))
des = float(input('Digite o valor do desconto a ser aplicado'))

cal = (pre / 100) * des
result = pre - cal

print('O valor do produto é de R${}\nO valor do desconto é de {}%\n'
      'O valor a ser pago é de R${}'.format(pre,des,result))