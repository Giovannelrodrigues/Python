numeros = 'zero', 'um', 'dois', 'três', 'quartro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze','treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'

num = int(input('Digite um valor de 0 á 20:'))
cont = 1

while cont > 0:
    if num >= 0 and num <=20:
        print(numeros[num])
        cont = 0

    else:
        num = int(input('Digite um valor de 0 á 20:'))