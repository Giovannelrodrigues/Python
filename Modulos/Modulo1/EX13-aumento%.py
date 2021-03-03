sal = float(input('Digite o valor do sálario'))
au = float(input('Digite o aumento em porcetagem'))

con = sal / 100 * au
result = sal + con

print('''Salário sem aumento é de R${}
      Porcentagem de aumento é de {}%
      valor do aumento é de R${}
      Salário com o aumento é de R${}'''.format(sal,au,con,result))