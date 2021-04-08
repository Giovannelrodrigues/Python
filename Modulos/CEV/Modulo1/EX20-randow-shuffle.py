import random
al1 = input('Digite o nome do aluno/grupo')
al2 = input('Digite o nome do aluno/grupo')
al3 = input('Digite o nome do aluno/grupo')
al4 = input('Digite o nome do aluno/grupo')

grupos = [al1, al2, al3, al4]
random.shuffle(grupos)

print('Esta é a ordem de apresentação{}')
print(grupos)