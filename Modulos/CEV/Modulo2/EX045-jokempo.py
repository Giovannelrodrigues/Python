import random

print('=' * 20)
print('Vamos jogar Jokempô')
print('=' * 20)
player = str(input('ESCOLHA UM'
                   '\nPEDRA'
                   '\nPAPEL'
                   '\nTESSOURA')).title().strip()

lista = ['Pedra', 'Papel', 'Tessoura']
sorteio = random.choice(lista)

if player == 'Pedra' and sorteio == 'Pedra':
    print('EMPATE, OS DOIS ESCOLHERAM PEDRA!!!')
elif player == 'Pedra' and sorteio == 'Tessoura':
    print('VOCÊ GANHOU!!, O COMPUTADOR ESCOLHEU TESSOURA')
elif player == 'Pedra' and sorteio == 'Papel':
    print('VOCÊ PERDEU!!, O COMPUTADOR ESCOLHEU PAPEL')
elif player == 'Papel' and sorteio == 'Papel':
    print('EMPATE, OS DOIS ESCOLHERAM PAPEL!!!')
elif player == 'Papel' and sorteio == 'Pedra':
    print('VOCÊ GANHOU!!, O COMPUTADOR ESCOLHEU PEDRA')
elif player == 'Papel' and sorteio == 'Tessoura':
    print('VOCÊ PERDEU!!, O COMPUTADOR ESCOLHEU TESSOURA')
elif player == 'Tessoura' and sorteio == 'Tessoura':
    print('EMPATE, OS DOIS ESCOLHERAM TESSOURA!!!')
elif player == 'Tessoura' and sorteio == 'Papel':
    print('VOCÊ GANHOU!!, O COMPUTADOR ESCOLHEU PAPEL')
elif player == 'Tessoura'and sorteio == 'Pedra':
    print('VOCÊ PERDEU!!, O COMPUTADOR ESCOLHEU PEDRA')
else:
    print('VOCÊ DIGITOU ERRADO, TENTE NOVAMENTE!!')