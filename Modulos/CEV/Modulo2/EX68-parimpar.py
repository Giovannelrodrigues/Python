from random import randint

win = lose  = 0
continuar = 1
print('=-=-=-=-=-=-=-=-=-=-=-=-=-')
print(' VAMOS JOGAR PAR OU IMPAR')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-')

while continuar == 1:
    player = int(input('Digite um valor:'))
    poui = str(input('Digite [P] para PAR OU [I] para IMPAR:')).strip()
    computer = randint(1,10)
    soma = player + computer

    if poui in 'Pp' and soma % 2 == 0:
        win += 1
        print('=================================================')
        print(f'Você Ganhou {player} + {computer} = {soma} = PAR')
        print('=================================================')


    elif poui in 'Pp' and soma % 2 == 1:
        lose += 1
        print('==================================================')
        print(f'Você Perdeu {player} + {computer} = {soma} = IMPAR')
        print('==================================================')


    elif poui in 'Ii' and soma % 2 == 1:
        win += 1
        print('==================================================')
        print(f'Você Ganhou {player} + {computer} = {soma} = IMPAR')
        print('==================================================')


    elif poui in 'Ii' and soma % 2 == 0:
        lose += 1
        print('=================================================')
        print(f'Você Perdeu {player} + {computer} = {soma} = PAR')
        print('=================================================')

    continuar = int(input('Você deseja continuar? [1]SIM [0]Não'))
    print('================================================')
    if continuar == 0:
        break
print('-----OBRIGADO POR JOGAR-----')
print(f'-----VOCÊ VENCEU {win} VEZES----')
print(f'-----VOCÊ PERDEU {lose} VEZES----')

