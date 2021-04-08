cont = 1
contidade = conthomem = contmulher = 0
continuar = 1
while continuar == 1:
    #contador
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    print(f'CADASTRO DA {cont}ª PESSOA')
    print('=-=-=-=-=-=-=-=-=-=-=-=')
    cont +=1

    idade = int(input('Digite a idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if idade > 17:
        contidade += 1
    if sexo in 'M':
        conthomem += 1
    if idade < 21 and sexo in 'F':
        contmulher += 1


    continuar = int(input('Deseja continuar? [0]Não [1]Sim:'))
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print(f'{contidade:^} são maiores de idade')
print(f'{conthomem} homens cadastrados')
print(f'{contmulher} mulher com menos de 20 anos')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')