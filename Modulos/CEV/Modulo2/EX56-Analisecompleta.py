#numeros de pessoas
num = int(input('Digite numero de pessoas'))

#variáveis
mediaidade = 0
quantmulher = 0
somaidade = 0
maisvelho = 0
nomevelho = ''
#estrutura de repetição
for p in range(1, num + 1):
    print('----{}ª PESSOA----'.format(p))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().title()
#média de idade
    mediaidade += idade
    somaidade = mediaidade / num
#mais velho
    if p == 1 and sexo == 'M':
        maisvelho = idade
        nomevelho = nome
    if sexo == 'M' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
#quantas mulheres
    if sexo  == 'F':
        quantmulher += 1

print('A média de idade das pessoas é de {} anos'.format(somaidade))
print('O homem mais velho possui {} anos e seu nome é {}'.format(maisvelho, nomevelho))
print('Nesse grupo de pessoas há {} mulhere/s'.format(quantmulher))



