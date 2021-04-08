def leia(num):
    while not num.isnumeric():
        num = str(input('Você Digitou errado, tente novamente:'))
    return num
    
n = leia(str(input('Digite um número:')))
print(f'Você digitou o número:{n}')
