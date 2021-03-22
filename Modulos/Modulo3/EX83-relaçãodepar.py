e = str(input('Digite sua expresão:'))
lista = []
for simb in e:
    if simb == '(':
        lista.append('(')
    if simb == ')':
        lista.pop()
if len(lista) > 0:
    print('Expresão nao pode ser concluida, pois está errada')
else:
    print('A expressão está correta')