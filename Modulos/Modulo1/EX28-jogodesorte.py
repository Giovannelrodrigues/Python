import random
print('Vamos jogar!,'
      '\nEu vou pensar em um número '
      '\nO seu objetivo é advinhar o número')
print('Nível de dificuldade'
            '\nFácil 0-5'
            '\nMédio 0-10'
            '\nDifícil 0-20'
            '\nImpossível 0-50')
dif = str(input('Digite o nível de dificuldade')).title().strip()
num = int(input('Digite o seu palpite'))

sortfa = random.randint(0,5)
sortme = random.randint(0,10)
sortdi = random.randint(0,20)
sortim = random.randint(0,50)

if dif == 'Fácil'and num == sortfa:
        print('Você Ganhou, o numero que eu pensei foi {}, Parabéns!!!'.format(num))
elif dif == 'Médio' and num == sortme:
        print('Você Ganhou, o numero que eu pensei foi {}, Parabéns!!!'.format(num))
elif dif == 'Difícil' and num == sortdi:
        print('Você Ganhou, o numero que eu pensei foi {}, Parabéns!!!'.format(num))
elif dif == 'Impossível'and num == sortim:
        print('Você Ganhou, o numero que eu pensei foi {}, Parabéns!!!'.format(num))
elif dif == 'Fácil'and num != sortfa:
        print('Você perdeu, o número que eu escolhi foi {}. Tente Novamente!!!'.format(sortfa))
elif dif == 'Médio' and num != sortme:
        print('Você perdeu, o número que eu escolhi foi {}. Tente Novamente!!!'.format(sortme))
elif dif == 'Difícil' and num != sortdi:
        print('Você perdeu, o número que eu escolhi foi {}. Tente Novamente!!!'.format(sortdi))
elif dif == 'Impossível'and num == sortim:
        print('Você perdeu, o número que eu escolhi foi {}. Tente Novamente!!!'.format(sortim))
else:
    print('Digite corretamente!')