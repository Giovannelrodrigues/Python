from datetime import date
nas = int(input('Digite o ano em que você nasceu'))
idade = date.today().year - nas

if idade < 10:
    print('Você faz parte da categoria MIRIN')
elif idade < 15:
    print('Você faz parte da categoria INFANTIL')
elif idade < 20:
    print('Você faz parte da categoria JUNIOR')
elif idade < 21:
    print('Você faz parte da categoria SENIOR')
else:
    print('Você faz parte da categoria MASTER')
