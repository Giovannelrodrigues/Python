matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = somacoluna = somalinha = 0
maior = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor[{linha + 1},{coluna + 1}]:'))
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^4}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            somacoluna += matriz[linha][coluna]
        if linha == 1:
            somalinha += matriz[linha][coluna]
    print()


print('=-=' * 10)
print(f'A soma de todos os números pares é de: {soma}')
print(f'A soma da 3ª coluna é de: {somacoluna}')
print(f'A soma da 2ª linha é de: {somalinha}')
