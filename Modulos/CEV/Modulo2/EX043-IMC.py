print('=' * 20)
print('Vamos calcular seu IMC!!!')
print('=' * 20)

peso = float(input('Digite seu peso em kilogramas'))
altura = float(input('Digite sua altura em metros'))

IMC = peso / altura**2

if IMC < 18.5:
    print('Você está abaixo do peso')
elif IMC < 26.0:
    print('Você está com peso ideal')
elif IMC < 31.0:
    print('Você está acima do peso')
elif IMC < 41.0:
    print('Você está obeso')
else:
    print('Você está em obesidade mórbida')
