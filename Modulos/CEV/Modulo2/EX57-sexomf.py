sexo = str(input('Digite seu sexo biológico [M/F]')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos, por favor tente novamente!')).strip().upper()[0]
print('Sexo {} salvo com sucesso'.format(sexo))