esc = 1 
contador = maior = menor= media = 0

while esc == 1:
        num = int(input('Digite um valor para somar a média:'))
        esc = int(input('Deseja continua [1]SIM [0]Não'))
            #média
        media += num
        contador += 1

        if contador == 1:
            maior = num
            menor = num
        elif num > maior:
            maior = num
        elif num < menor:
            menor = num
        

somamedia = media / contador
print('===================================================')
print('A média dos números digitados é de {}'.format(somamedia))
print('O maior valor é de {} e o menor digitado é de {}'.format(maior,menor))
print('===================================================') 


