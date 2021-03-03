nome = input('Digite seu nome completo').strip()
print('Seu nome tudo maiúsculo é {}'.format(nome))
print('Seu nome tudo minúsculo é {}'.format(nome.lower()).upper())
print('Seu nome possui {} letras'.format(len(nome)-nome.count(' ')))

#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro é {} e possui {} letras'.format(separa[0], len(separa[0])))