print('=' * 20)
print('Analizando triângulo......')
print('=' * 20)
lado1 = int(input('Digite o primeiro seguimento de reta'))
lado2 = int(input('Digite o segundo seguimento de reta'))
lado3 = int(input('Digite o terceiro seguimento de reta'))

menor = lado1
if lado2 < lado1 and lado2 < lado3:
    menor = lado2
elif lado3 < lado1 and lado3 < lado2:
    menor = lado3

maior = lado2
if lado1 > lado2 and lado1 > lado2:
    maior = lado1
elif lado3 > lado2 and lado3 > lado1:
    maior = lado3

meio = lado3
if lado1 > menor and lado1 < maior:
    meio = lado1
elif lado2 > menor and lado2 <maior:
    meio = lado2

soma = menor + meio
if soma > maior:
    print('É possível fazer um triângulo com esses seguimentos!!!')
    if lado1 == lado2 and lado1 == lado3:
        print('A nomenclatura do seu triângulo é EQUILÁTERO, pois possui todos os lados com o mesmo valor')
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print('A nomenclatura do seu triângulo é ESCALENO, pois possui todos os lados com valores diferentes')
    else:
        print('A nomenclatura do seu triângulo é ISÓCELES, pois possui dois lado com valores iguais')
else:
    print('Não é possível fazer um triângulo com esses seguimentos!!!')

