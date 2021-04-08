Jogador = {}
jogos = {}
contador = gols = 0

Jogador['Nome'] = str(input('Digite o nome do jogador:'))
partidas = int(input('Digite quantas partidas ele jogou:'))

while contador < partidas:
    contador += 1

    gol = int(input(f'Quantos gols fez no {contador}ª jogo:'))
    jogos[f'Jogo{contador}'] = gol
    gols += gol

Jogador['Gols'] = jogos
Jogador['Total'] = gols

print('=' * 30)
print(Jogador)
print('=' * 30)
print(f'O nome do jogador é: {Jogador["Nome"]}')
print(f'Os gols: {jogos}')
print(f'Total de gols {Jogador["Total"]}')
print('=' * 30)
print(f'O jogador: {Jogador["Nome"]} jogou {partidas} vezes')
contador = 0
for contador in range(1,partidas + 1):
    print(f'No Jogo {contador} fez:', jogos[f'Jogo{contador}'])
print(f'Total de gols {Jogador["Total"]}')
print('=' * 30)