from random import randint

sorteios = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)

for cont in sorteios:
    print(f'{cont} -->', end='')

print(f'\nO maior número sorteado foi o {max(sorteios)}')
print(f'O menor número sorteado foi o {min(sorteios)}')