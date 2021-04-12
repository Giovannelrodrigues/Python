import re #RegEx
#texto
texto = "Curso de Python do CFB Cursos, canal no Youtube"
print(texto)
pesquisa = input('Digite oquer pesquisar no texto:')

#proucura palavra no texto
res=re.search(pesquisa,texto)
#retona a posição em que foi encontrada

try:
#inicial
    inicial = (res.start())

    #posição em que termina
    final = (res.end())

    #tamanho da string
    tamanho = res.end() - res.start()
except AttributeError:
    print('Não encontrado')
except:
    print('Erro')
else:
    print(f'posição inicial: {inicial}')
    print(f'posição final: {final}')
    print(f'Tamanho: {tamanho}')

