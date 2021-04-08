lista = []
contador = 0
continuar = 'S'

def analise(listaNumeros):
    """
    parametro é uma lista com notas inserida pelo usario
    retorno é um dicionario com informação
    """
    dic = {}
    dic['Total'] = len(listaNumeros)
    dic['MaiorNota'] = max(listaNumeros)
    dic['MenorNota'] = min(listaNumeros)
    dic['Média'] = sum(listaNumeros) / len(listaNumeros)
    if dic['Média'] <= 2:
        dic['Situação'] = 'Péssima'
    elif dic['Média'] <= 4:
        dic['Situação'] = 'Ruim'
    elif dic['Média'] <= 6:
        dic['Situação'] = 'Mediana'
    elif dic['Média'] <= 8:
        dic['Situação'] = 'Muito Bom'
    elif dic['Média'] <= 10:
        dic['Situação'] = 'Execelente'
    
    return dic
   
while continuar == 'S':
    #Pegar notas e colocar em uma lista
    contador +=1
    nota = float(input(f'Digite a {contador}ª nota:'))
    while nota > 10:
         nota = float(input(f'Digite a {contador}ª nota:[0 até 10]'))
    lista.append(nota)
    #para adicionar quantas notas quiser
    continuar = str(input('Deseja continuar? [S/N]')).strip().title()[0]

dic = analise(lista)
print(dic)
print('<==ENCERRADO==>')

#É possivel fazer apenas com o método e inserir o valor no parametro do método usando 
# \=====(<\=/>)=====/ def analise(*num, sit=False) \======(<\=/>)=====/
