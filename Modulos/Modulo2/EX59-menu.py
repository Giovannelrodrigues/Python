num1 = int(input('Primeiro valor'))
num2 = int(input('Segundo valor'))
op = 0
maior = 0

while op !=5:
    op = int(input('''
    ====================
    Soma             = 1
    Multiplicar      = 2
    Maior            = 3
    Novos números    = 4
    Sair do Programa = 5
    ====================
    Digite uma opção:'''))
    
#soma
    if op == 1:
        soma = num1 + num2
        print('''=========================
A soma entre {} + {} = {}
========================='''.format(num1, num2, soma))
#Multiplicação   
    if op == 2:
        soma = num1 * num2
        print('''============================
O produto entre {} * {} = {}
============================'''.format(num1, num2, soma))
    if op == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(''''============================
Entre {} e {} o maior é {}
============================'''.format(num1, num2, maior))
    if op == 4:
        num1 = int(input('Primeiro valor'))
        num2 = int(input('Segundo valor'))
print('PROGRAMA ENCERRADO!')