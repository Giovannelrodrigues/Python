c = ('\033[m',
    '\033[0;30;41m',
    '\033[0;35,41m' )

def ajuda(txt):
    help(txt)

def título(msg,cor=0):
    print(c[cor], end='')
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
while True:
    título('SYSTEM OF HELP (PyHelp)', 1)
    nome = str(input('Digite a função ou biblioteca:'))
    if nome.upper() == 'FIM':
        break
    else:
        ajuda(nome)
título('Volte Sempre',2)

#é possivel fazer um lista de cores e usar ela como parametro