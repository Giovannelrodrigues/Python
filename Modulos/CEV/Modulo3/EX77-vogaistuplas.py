palavras = 'APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO'

for contador in palavras:
    print(f'Na palavra: {contador} temos: ', end='')
    for letra in contador:
        if letra.lower() in 'aeiouáíéõãâêô':
            print(letra.lower(),'', end='')
    print('\n')