al = str(input('Digite uma frase')).lower().strip()
print('A letra A aparece {} vezes'.format(al.count('a')))
print('A primeira letra A apareceu na posição {}'.format(al.find('a') + 1))
print('A ultima letra A apareceu na posição {}'.format(al.rfind('a') + 1))