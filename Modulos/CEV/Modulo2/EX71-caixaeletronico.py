
print('=' * 25)
print('{:^25}'.format('BANCO DO MOSCOU'))
print('=' * 25)

saque = int(input('Digite o valo que deseja sacar:'))
montant = saque
ced50 = 50
ced20 = 20
ced10 = 10
ced5 = 5
ced1 = 1
cont1 = cont5 = cont10 = cont20 = cont50 = 0

while montant != 0:
    if montant > ced50:
        cont50 = montant // ced50
        resto = montant % ced50
        montant = resto
    elif montant == ced50:
        montant = 0
        cont50 += 1
    if montant > ced20:
        cont20 = montant // ced20
        resto = montant % ced20
        montant = resto
    elif montant == ced20:
        montant = 0
        cont20 += 1
    if montant > ced10:
        cont10 = montant // ced10
        resto = montant % ced10
        montant = resto
    elif montant == ced10:
        montant = 0
        cont10 += 1
    if montant > ced5:
        cont5 = montant // ced5
        resto = montant % ced5
        montant = resto
    elif montant == ced5:
        montant = 0
        cont5 += 1
    if montant > ced1:
        cont1 = montant // ced1
        resto = montant % ced1
        montant = resto
    elif montant == ced1:
        montant = 0
        cont1 += 1

print('=' * 25)        
print(f'Sairam {cont50} cedulas de R${ced50}')
print(f'Sairam {cont20} cedulas de R${ced20}')
print(f'Sairam {cont10} cedulas de R${ced10}')
print(f'Sairam {cont5} cedulas de R${ced5}')
print(f'Sairam {cont1} cedulas de R${ced1}')
print('=' * 25)