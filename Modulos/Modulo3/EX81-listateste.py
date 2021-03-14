continuar = 'S'
contador = cont5 = 0
lista = []
a = 0
while continuar == 'S':
    num = int(input('Digite um valor:'))
    lista.append(num)
    contador += 1
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

for i, c in enumerate(lista):
    if lista[i] == 5:
        a += 1
    i += 1
lista.sort(reverse=True)
print('='*40)
print(f'Você digitou {contador} elementos')
print(f'A ordem decrescente dessa lista:{lista}')

if a > 0: 
    print('O número 5 faz parte dessa lista')
else:
    print('O número 5 não faz parte dessa lista')
print('='*40)