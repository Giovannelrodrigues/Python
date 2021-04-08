frase = str(input('Digite uma frase')).strip().upper()
sep = frase.split()
jun = ''.join(sep)
inv = ''
for poli in range(len(jun)-1, -1,-1):
    inv += jun[poli]
if inv == jun:
    print('A frase {} é um palíndromo e fica {}'.format(frase, inv))
else:
    print('A frase {} não é um palíndromo e fica {}'.format(frase, inv))