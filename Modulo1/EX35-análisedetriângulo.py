print('=' * 20)
print('Analizando triângulo......')
print('=' * 20)
r1 = float(input('Digite o primero sequimento de reta'))
r2 = float(input('Digite o segundo sequimento de reta'))
r3 = float(input('Digite o terceiro seguimento de reta'))

menor = r1
if r2 < r1 and r2 < r3:
    menor = r2
if r3 < r2 and r3< r1:
    menor = r3

maior = r3
if r2 > r3 and r2 > r1:
    maior = r2
if r1 > r2 and r1 >r3:
    maior = r1

meio = r2
if r1 > menor and r1 < maior:
    meio = r1
if r3 > menor and r3 < maior:
    meio = r3

soma = menor + meio
if soma > maior:
    print('O seguimento de reta forma uma triângulo!')
else:
    print('O seguiemnto de reta não forma um triângulo')