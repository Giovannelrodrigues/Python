print('=' * 20)
print('Condição de pagamento')
print('=' * 20)
preco = float(input('Digite o valor do produto'))
print('=' * 20)
forma = int(input('\n[1] DINHEIRO/CHEQUE'
                  '\n[2] DÉBITO'
                  '\n[3] PARCELA 2X'
                  '\n[4] PARCELA 3X OU MAIS'
                  '\nDigite a forma de pagamento'))

if forma == 1:
    soma = preco - preco / 100 * 10
    print('O valor a ser pago é de R${}'.format(soma))
elif forma == 2:
    soma = preco - preco / 100 * 5
    print('O valor a ser pago é de R${}'.format(soma))
elif forma == 3:
    print('O valor a ser pago é de R${}'.format(preco))
elif forma == 4:
    soma = preco + preco / 100 * 20
    print('O valor a ser pago é de R{}'.format(soma))
else:
    print('Forma de Pagamento Inválida, TENTE NOVAMENTE!!')

