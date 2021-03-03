km = int(input('Quantos Km a sua viagem possui?'))

if km <= 200:
    print('O valor para {}Km são R${}'.format(km,km * 0.50))
else:
    print('O valor para {}Km são R${}'.format(km,km * 0.45))