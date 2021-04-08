def voto(a):
    """
    Ver se a pessoa é obrigatório, opcinonal ou se nao pode votar!
    a = ano de nascimento
    """
    from datetime import date
    resp = date.today().year - ano
    if resp <= 15:
        return f'Com {resp}:Você ainda não pode votar'
    if resp >= 18:
        return f'Com {resp}:Você é obrigado a votar'
    if resp > 15 and resp < 18:
        return f'Com {resp}:Você pode escolher votar ou não'

ano = int(input('Digite o ano que você nasceu'))
resposta = voto(ano)

print(resposta)

