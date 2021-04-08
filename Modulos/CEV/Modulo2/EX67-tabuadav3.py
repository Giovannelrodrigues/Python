contador = 1
tab = int(input('Digite o valor da tabuada:'))
while True:
    print(f'{tab} X {contador} = {tab * contador}')
    contador += 1
    if contador > 10:
        print('Para encerrar o programa digite [0]')
    if contador > 10:
        tab = int(input('Digite o valor da tabuada:'))
        contador = 0
    if tab < 1:
        break
print('FIM, VOLTE SEMPRE!')