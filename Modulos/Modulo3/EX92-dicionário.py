from datetime import date
dados = {}

dados['Nome'] = str(input('Digite seu nome:'))
ano = int(input('Digite o ano que você nasceu:'))
dados['Idade'] = date.today().year - ano
dados['Ctps'] = int(input('Digite sua carteira de trabalho: (0 Caso não tenha)'))
dados['Sexo'] = str(input('Digite seu Sexo Biológico: [M/F]')).strip().upper()[0]

if dados['Ctps'] == 0:
    print(f'Seu nome é: {dados["Nome"]}')
    print(f'Sua idade é de: {dados["Idade"]}')
    print(f'Não possui carteira de trabalho')

if dados['Ctps'] != 0:
    dados['AnoTrabalho'] = int(input('Digite em que ano foi contratado'))
    dados['Sálario'] = float(input('Digite seu sálario R$ '))

    print('=' * 30)
    print(f'Seu nome é: {dados["Nome"]}')
    print(f'Sua idade é de: {dados["Idade"]}')
    print(f'O número da dua Ctps: {dados["Ctps"]}')
    print(f'Ano de contratação foi em: {dados["AnoTrabalho"]}')
    print(f'O seu sálario é de: {dados["Sálario"]}')

    if dados['Sexo'] == 'M' and dados['Idade'] < 66:
        aposentadoria = 65 - dados['Idade']
        print(f'Falta {aposentadoria} anos para você se aposentar')
        print(f'Sexo Masculino')
    if dados['Sexo'] == 'F' and dados['Idade'] < 63:
        aposentadoria = 62 - dados['Idade']
        print(f'Falta {aposentadoria} anos para você se aposentar')
        print(f'Sexo Feminino')
    if dados['Idade'] >= 65 and dados['Sexo'] == 'M':
        aposentadoria = dados['Idade'] - 65
        print(f'Você ja é aposentado há {aposentadoria} anos')
    if dados['Idade'] >= 62 and dados['Sexo'] == 'F':
        aposentadoria = dados['Idade'] - 62
        print(f'Você ja é aposentada há {aposentadoria} anos')