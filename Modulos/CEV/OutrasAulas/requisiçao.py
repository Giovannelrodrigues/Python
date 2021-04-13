import requests

def retorna_dado_cep(cep):
    res = requests.get('https://viacep.com.br/ws/01001000/json/')
    #print(res.status_code) 200 = funcionando 400= não funcionando
    dados = res.json() #tranformando em dicionário
    print(dados['cep'])


def retorna_dados_pokemon(pokemon):
    reponse = requests.get(f'https://pokeapi.co/api/v2/{pokemon}/')
    dados_pokemon = reponse.text
    print(dados_pokemon)

def retorna(url):
    response = requests.get(url)
    return response.text

resp = retorna('https://www.linkedin.com/in/giovanne-rodrigues-9b07ab205/')
print(resp)