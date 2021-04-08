total = 0
preco = 0
quant = 0
nome = ''
continuar = 'S'
nmb = ''

print('=-=-=-=-=-=-=-=-=')
print('LOJINHA DO MOSCOU')
print('=-=-=-=-=-=-=-=-=')

while continuar == 'S':

    maior = preco
    maiorq = preco * quant
    maisb = preco
    nmb = nome

    #info do produto
    nome = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o preço do produto:'))
    quant = int(input('Digite a quantidade:'))

    #somatotal
    total += preco * quant

    #mais caro
    if preco > maior:
        maior = preco
        
    #mais caro em quantidade
    if quant * preco > maiorq:
        maiorq = quant * preco
        precou = maiorq / quant

    #nome mais barato
    if preco < maisb:
        maisb = preco
        nmb = nome

    continuar = str(input('Deseja continuar [S/N]')).strip().upper()[0]
print('=-=-=-=-=-=-=-=-=-=-=-=')
print(f'O preço final ficou de R${total}')
print(f'O protudo com maior preço custou R${maior}')
print(f'O produto  mais caro em quantidade custou {maiorq}, porém cada unidade custa R${precou}')
print(f'O nome do produto mais barato é {nmb} e custou R${maisb} a unidade')
print('=-=-=-=-=-=-=-=-=-=-=-=')