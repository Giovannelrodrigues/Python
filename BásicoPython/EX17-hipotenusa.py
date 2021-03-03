from math import sqrt
co = float(input('Digite o valor do cateto oposto'))
ca = float(input('Digite o valor do cateto adjacente'))

hip = co**2 + ca**2
raiz = sqrt(hip)
print('O valor da hipotenusa é de {}'.format(raiz))