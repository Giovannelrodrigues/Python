nome = str(input('Digite seu nome completo')).strip().title()
n = nome.split()
print('Muito prazer em te conhecer')
print('Seu priemiro nome é {}'.format(n[0]))
print('Seu ultimo nome é {}'.format(n[len(n) - 1]))