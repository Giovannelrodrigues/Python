def imprimir(txt):
    print('=' * len(txt))
    print(f'{txt}')
    print('=' * len(txt))

imprimir(str(input('Digite uma frase:')))