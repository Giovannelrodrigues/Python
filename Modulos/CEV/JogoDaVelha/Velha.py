import os
import random
from colorama import Fore

matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
linha = coluna = 0
jogadas = 0
maxJogadas = 9
quemJoga = 0 #0cpu 1- player
markJogador = ''
markComputador = 'X'
vitoriasComputador = vitoriasJogador = 0
continuar = 'S'

def telaDoJogo():
        os.system('cls')
        print(f'   0   1   2')
        print(f'0: {matriz[0][0]} | {matriz[0][1]} | {matriz[0][2]}')
        print(f'--------------')
        print(f'1: {matriz[1][0]} | {matriz[1][1]} | {matriz[1][2]}')
        print(f'--------------')
        print(f'2: {matriz[2][0]} | {matriz[2][1]} | {matriz[2][2]}')
        print(f'Jogadas: {Fore.GREEN + str(jogadas) + Fore.RESET}')

def escolha():
    global markJogador
    global markComputador
    markJogador = str(input('Digite a Tecla que deseja Marcar')).strip().upper()[0]
    if markJogador == 'X':
        markComputador = 'O'

def sorteioComeçar():
    global quemJoga
    quemJoga = random.randint(0,1)

def computador():
    global quemJoga
    global jogadas
    global maxJogadas
    global markComputador
    if quemJoga == 0 and jogadas < maxJogadas:
        try:
            l = random.randint(0,2)
            c = random.randint(0,2)
            while matriz[l][c] != ' ':
                l = random.randint(0,2)
                c = random.randint(0,2)
        except:
            print('ocorreu um erro, tente reiniciar')
        else:
            matriz[l][c] = markComputador
            jogadas +=1
            quemJoga = 1

def jogador():
    global quemJoga
    global jogadas
    global maxJogadas
    global markJogador
    if quemJoga == 1 and jogadas < maxJogadas:
        try:
            l = int(input('linha...:'))
            c = int(input('Coluna..:'))
            while matriz[l][c] != ' ':
                l = int(input('linha...:'))
                c = int(input('Coluna..:'))
        except:
            print('ocorreu um erro, tente reiniciar')
        else:
            matriz[l][c] = markJogador
            jogadas += 1
            quemJoga = 0

def analise():
        

while continuar == 'S':
    escolha()
    sorteioComeçar()
    while jogadas <= maxJogadas:
        telaDoJogo()
        jogador()
        computador()
        if jogadas == 9:
            break
    telaDoJogo()
    
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
