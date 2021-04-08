def mostrar(j, g):
    print(f'O {j} fez {g} no campeonato')


jogador = str(input('Nome do jogador:'))
gols = str(input('Quantos gols ele fez?'))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    jogador = str('<Desconhecido>')
mostrar(jogador,gols)
