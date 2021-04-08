def area(lar, com):
    areaTerreno = lar * com
    print(f'O terreno de {lar}x{com} é igual: {areaTerreno}m quadrados')

lar = int(input('Digite a largura:'))
com = int(input('Digite o comprimento:'))
area(lar, com)