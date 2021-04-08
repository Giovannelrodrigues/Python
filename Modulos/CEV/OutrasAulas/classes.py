class Carro:
    velMax=0
    ligado=False
    cor=''

c1=Carro()
c2=Carro()
c3=Carro()

c1.velMax = 200
c1.ligado = False
c1.cor='Prata'

c2.velMax = 250
c2.ligado = True
c2.cor='Preto'

c3.velMax = 220
c3.ligado = True
c3.cor='Vermelho'

if c1.ligado == True:
    estado = 'ligado'
else:
    estado = 'Desligado'
    
print(f'Velocidade maxima: {c1.velMax}')
print(f'Ligado ou Desligado: {estado}')
print(f'Cor {c1.cor}')