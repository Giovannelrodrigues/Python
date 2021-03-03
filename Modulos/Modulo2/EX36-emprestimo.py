casa = int(input('Digite o valor da casa que deseja financiar'))
sal = float(input('Digite o valor da sua renda mensal'))
parcelas = int(input('Em quantas parcelas você deseja pagar'))

pres = casa / parcelas
tri = sal / 100 * 30

if pres <= tri:
    print('O seu empréstimo foi aprovado!!!'
          '\nO valor do emprestimo é de R${}'
          '\nO valor de cada parcela é de R${:.2f}'
          '\nA quantidade de parcelas {}x'.format(casa,pres,parcelas))
else:
    print('Você ainda não está apto para realizar esse empréstimo')
