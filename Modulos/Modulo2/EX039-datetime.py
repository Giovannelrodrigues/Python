from datetime import date
ano = int(input('Digite o ano em que você nasceu'))
ali = date.today().year - ano

if ali < 18:
    print('Você não está em período de alistamento ainda falta {} anos'.format(18 - ali))
elif ali == 18:
    print('Você deve se alistar nas forças armadas esse ano')
else:
    print('Você ja passou do período de alistamento')


