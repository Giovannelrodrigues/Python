listaJogadores = []
dadosJogares = {}
listaGols = []

continuar = 'S'
Jogos = contador = cont = soma = c = num = indice = contador2 = 0

while continuar == 'S':
    #ler nome e quant de partidas
    dadosJogares['Nome'] = str(input('Digite o nome do jogador:'))
    partidas = int(input('Quantos ele Jogou?'))
    #zerando para outro jogador
    contador = cont = soma = num = 0
    #lendo gols de cada partida
    while contador < partidas:
        contador +=1

        num = int(input(f'Quanto gols {dadosJogares["Nome"]} fez no {contador}ª jogo:'))
        #total de 
        soma += num
        dadosJogares['Total'] = soma
        #lista dos gols
        listaGols.append(num)
    #jogando lista gols no d
    dadosJogares['Gols'] = listaGols[:]
    dadosJogares['Ind'] = indice
    indice += 1
    listaGols.clear()
    listaJogadores.append(dadosJogares.copy())

    continuar = str(input('Deseja Continuar? [S/N]')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Digite SIM ou Não:')).strip().upper()[0]

c = 0
for t in listaJogadores:
    print(f'{c} Nome:{t["Nome"]} Gols:{t["Gols"]}  Total:{t:["Total"]}')
    c += 1

resp = 0
while resp != 999:
    ca = 0
    resp = int(input('Digite o valor do indice do jogador para mais informação. Se não quizer digite [999]:'))
    for pessoa in listaJogadores:
        if resp == pessoa["Ind"]:
            for contador2 in pessoa["Gols"]:
                print(f'No {ca + 1}ª jogo fez: {pessoa["Gols"][ca]}')
                ca += 1
print('===VOLTE SEMPRE===')

   