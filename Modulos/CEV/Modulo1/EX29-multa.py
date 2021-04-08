vel = int(input('Qual é a velocidade do carro'))

if vel > 80:
    print('Você foi multado em R${}, acima da velocidade permitida de 80KM/h'.format((vel - 80) * 7))
else:
    print('Você está {}KM/h, continue dirigindo com segurança :)'.format(vel))