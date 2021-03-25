dados = {}
notas = somaNotas = media = 0

dados['Nome'] = str(input('Digite o nome do aluno:'))
for c in range(1,5):
    notas = int(input(f'Digite a {c}ª nota:'))
    somaNotas += notas
media = somaNotas / 4
dados['Média'] = media

if media >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'

print('=' * 30)
print(f'O nome do aluno é {dados["Nome"]}')
print(f'A média do aluno é de: {dados["Média"]}')
print(f'A situacão do aluno é {dados["Situação"]}')
print('=' * 30)


