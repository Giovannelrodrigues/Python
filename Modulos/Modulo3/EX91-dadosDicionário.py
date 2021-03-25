from random import randint
from time import sleep
from operator import itemgetter
Numeros = {}
rank = list()

for contador in range(1,5):
    Numeros[f'Player{contador}'] = randint(1,6)
    print(f'Player{contador} tirou {Numeros[f"Player{contador}"]}')
    sleep(1)

rank = sorted(Numeros.items(), key=itemgetter(1), reverse=True)
print('='* 30)
print("O ranking dos Jogadores")
for ind, valor in enumerate(rank):
    print(f'{ind + 1}ª lugar = {valor[0]} tirou {valor[1]}')
    sleep(1)
print('='* 30)
   
    
