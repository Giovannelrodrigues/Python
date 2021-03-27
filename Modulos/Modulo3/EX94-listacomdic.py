pessoas = []
listaMulheres = []
dados = {} 

continuar = 'S'
contador = somaIdade = media = 0

while continuar == 'S':
    #dados no diconário
    dados['Nome'] = str(input('Digite um nome: '))
    dados['Sexo'] = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
    while dados['Sexo'] != 'M' and dados['Sexo'] != 'F':
        dados['Sexo'] = str(input('[M/F] Digite seu sexo: ')).strip().upper()[0]
    dados['Idade'] = int(input('Digite sua Idade: '))
    pessoas.append(dados.copy())

    #contador
    contador += 1

    #coma das idadesd
    somaIdade += dados['Idade']

    #mulheres
    if dados['Sexo'] == 'F':
        listaMulheres.append(dados['Nome'])

    #verificar se deseja continuar
    continuar = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    while continuar not in 'SsNn':
        continuar = str(input('Digite Sim ou Não: Deseja continua?')).strip().upper()[0]

#média das idades
media = somaIdade /contador

print(f'=== {contador} FORAM CADASTRADA ===')
print(f'A média da idade é de: {media}')
print(f'Mulheres cadastradas {listaMulheres}')

#pessoas acima da média da idade:
for dicionario in pessoas:
    if dicionario['Idade'] >= media:
        print(dicionario)
print('<====ENCERRADO====>')