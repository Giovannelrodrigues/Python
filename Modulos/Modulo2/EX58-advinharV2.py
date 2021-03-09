import random

#variáveis
tent = 0
acertar = False

print('=' * 50)
dif = int(input('''Vamos jogar, eu vou escolher um número e seu objetivo é adivinhar em poucas tentativas
    ==============
    Fácil      = 1
    Médio      = 2
    Díficil    = 3
    Impossível = 4
    ==============
Digite a dificuldade:'''))

#Nivel de dificuldade 
fa = random.randint(1,5)
me = random.randint(1,10)
di = random.randint(1,20)
im = random.randint(1,50)
#Nivel fácil
if dif == 1:
    while not acertar:
        pal = int(input('Digite seu palpite de 1 á 5:'))
        tent += 1
        if pal == fa:
            acertar = True
        else:
            print('Valor inválido, tente novamente!!!')
            if pal < fa and pal < 6:
                print('Mais... você errou, tente novamente!')
            elif pal > fa and pal < 6:
                print('Menos... você errou, tente novamente')
    print('Você acertou, o número era {}, você usou {} tentativa/s'.format(fa,tent))

#Nivel médio
if dif == 2:
    while not acertar:
        pal = int(input('Digite seu palpite de 1 á 10:'))
        tent += 1
        if pal == me:
            acertar = True
        else:
            print('Valor inválido, tente novamente!!!')
            if pal < me and pal < 11:
                print('Mais... você errou, tente novamente!')
            elif pal > me and pal < 11:
                print('Menos... você errou, tente novamente!')
    print('Você acertou, o número era {}, você usou {} tentativa/s'.format(me,tent))

#Nivel Dificil
if dif == 3:
    while not acertar:
        pal = int(input('Digite seu palpite de 1 á 20:'))
        tent += 1
        if pal == di:
            acertar = True
        else:
            print('Valor inválido, tente novamente!!!')
            if pal < di and pal < 21:
                print('Mais... você errou, tente novamente!')
            elif pal > di and pal < 21:
                print('Menos... você errou, tente novamente!')
    print('Você acertou, o número era {}, você usou {} tentativa/s'.format(di,tent))

#Impossível
if dif == 4:
    while not acertar:
        pal = int(input('Digite seu palpite de 1 á 50:'))
        tent += 1
        if pal == im:
            acertar = True
        else:
            print('Valor inválido, tente novamente!!!')
            if pal < im and pal < 51:
                print('Mais... você errou, tente novamente!')
            elif pal > im and pal < 51:
                print('Menos... você errou, tente novamente!')
    print('Você acertou, o número era {}, você usou {} tentativa/s'.format(im,tent))
else:
    print('Valor inválido, tente novamente!!!')


