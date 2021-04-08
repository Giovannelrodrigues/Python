try:
    x=10
    print(x)
except TypeError:
    print('ERRO DE TIPO')
except KeyboardInterrupt:
    print('Valor não foi inserido')
except:
    print('ERRO')
else:
    print('Não houve "ERRO"')
finally:
    print('Volte Sempre')

#
num = 18
if num < 1:
    raise Exception('Valor Não Permitido')
num = 'A'
if not type(num) is int():
    raise Exception('Somente NÚMEROS')
