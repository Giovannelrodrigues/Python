pt = int(input('Digite o valor do primeiro termo:'))
ra = int(input('Digite o valor da razão:'))
nu = int(input('Quantos termos você precisa?'))
termo = pt + ((nu + 1)-1) * ra
for pa in range(pt,termo,ra):
    print(pa,'-->')
