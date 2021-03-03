import random
al1 = input('Digite o nome do aluno')
al2 = input('Digite o nome do aluno')
al3 = input('Digite o nome do aluno')
al4 = input('Digite o nome do aluno')

alunos = [al1,al2,al3,al4]
sort = random.sample(alunos,1)

print('O aluno escolhido foi o/a {}'.format(sort))