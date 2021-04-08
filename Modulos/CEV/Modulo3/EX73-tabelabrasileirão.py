tabela = 'Flamego', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba', 'Botafogo'

print(f'Os cinco primeiros colocados são os times:{tabela[0:5]}')
print('=' * 50)
print(f'Os cinco ultimos colocados são os times: {tabela[-4:]}')
print('=' * 50)
print(f'Os Times em ordem alfabetica {sorted(tabela)}')
print('=' * 50)
sp = tabela.index('São Paulo')
print(f'O time do São Paulo está em {sp + 1}ª colocado')
print('=' * 50)