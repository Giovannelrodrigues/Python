num = int(input('Digite um valor inteiro'))
base = int(input('Escolha a base de conversão'
                 '\n[1] Para base BINÁRIA'
                 '\n[2] Para base OCTAL'
                 '\n[3] Para base Hexadecimal'
                 '\nEscolha um Opção:'))

if base == 1:
    print('O número {}, convertido para Binário é {}'.format(num, bin(num)[2::]))
elif base == 2:
    print('O número {}, convertido para Octal é {}'.format(num, oct(num)[2::]))
elif base == 3:
    print('O número {}, convertido para hexadecimal é {}'.format(num, hex(num)[2::]))
else:
    print('Você escolheu uma base de conversão inválida, TENTE NOVAMENTE!!!')


