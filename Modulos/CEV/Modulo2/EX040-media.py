n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite sua segunda nota'))

me = (n1 + n2) / 2

if me > 6.9:
    print('O aluno foi APROVADO, Sua média é de {}'.format(me))
elif me < 5:
    print('O Aluno foi REPROVADO, Sua média é de {}'.format(me))
else:
    print('O aluno está de RECUPERAÇÃO, Sua média é de {}'.format(me))