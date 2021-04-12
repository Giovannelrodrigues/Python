#nome = 'ManipulaçãoDeArquivo.txt'
#arquivo=open(f'C:/teste/{nome}', 'r')
#r - read (se não houver ele cria sosinho)
#a = append
#w - write (se não houver ele criar sosinho)
#x = create
#t - text
#b = binário


#print(arquivo.read(10)) #imprime os 10 primeiro caracteres

#print(arquivo.readline())
#readline retorna uma string
#for l in arquivo:
    #print(l) 


#
# Aula 3
#
print("=================")

import os
nome = 'ManipulaçãoDeArquivo.txt'
caminho = 'C:/teste/'
caminhoComNome = f'{caminho}{nome}'

if os.path.exists(caminhoComNome):
    print('Arquivo Encontrdado')
else:
    arquivo=open(caminhoComNome, 'x')
    print('Arquivo criado')
    arquivo.close()

if os.path.exists(caminhoComNome):
    os.remove(caminhoComNome)
    print('Arquivo removido')
else:
    print('Arquivo Não Encontrado')
