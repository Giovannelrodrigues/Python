import datetime

#data e hora atual
data = datetime.datetime.now()
#data passada como parametro
nas = datetime.datetime(2003,6,20)
#strftime para indicar formato
print(nas.strftime('#abaixo escolha'))

#Dia da semena(texto): %A
#Sigla da semena(texto): %a
#Numero do dia da semana(num) %w  (domingo = 0, segunda = 1)
#Dia do mês: %d
#Sigla mês(texto): %b
#Nome mês(texto): %B
#Número do mês(num): %m
#Ano com dois digitos(num): %y
#Ano completo(num):%Y
#Hora 2 digitos(num): %H (00 - 23)
#Hora 2 digitos(num): %I (00 - 12)
#AM or PM(texto): %p
#Minutos: %M
#Segundos %S
#MicroSegundos %f
#Dia do ano(num): %j (001-365)
#Número da semana do ano: %W

