primeiro = int(input('Digite o primeiro valor:'))
razao = int(input('Digite a razão:'))
numdetermos = int(input('Digite quantos termos você quer'))
ter1 = primeiro
mais = 1
contador = 0

while mais != 0:
    while numdetermos > 0:
        print('{}-->'.format(primeiro), end='')
        primeiro += razao
        numdetermos -= 1
        contador += 1
    numdetermos = int(input('\nVoce deseja mostrar mais algum termo? Se não digite [0]'))
    mais = numdetermos
print('FIM, O tatal de termos que apareceram foi {}'.format(contador))
