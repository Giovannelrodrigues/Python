import json

#criar um json
carros_json = '{"Marca":"Honda","Modelo":"HRV","Cor":"Branca"}'
carros=json.loads(carros_json)

for k,v in carros.items():
    print(f'{k} = {v}')

#converter em Json:
carros2 = {"Marca":"Honda","Modelo":"HRV","Cor":"Branca"}
carros2_json=json.dumps(carros2)
print(carros2)

#===============#
#=====AULA2=====#
#===============#
print('==========================')
import json

carros_dic={"Marca":"Honda","Modelo":"HRV","Cor":"Branca"}
#dic -> objeto json

carros_lista=["Marca","Honda","Modelo","HRV","Cor","Branca"]
#list - > array json

carros_tupla=("Marca","Honda","Modelo","HRV","Cor","Branca")
#tupla -> array json

# indent=2 parametro para dar indentação
# substituir (separators=(':','='))
# sort_keys=True = ordem alfabetica das chaves
carros_j=json.dumps(carros_dic,indent=2,separators=(':','='), sort_keys=True)
carros_jt=json.dumps(carros_tupla)
carros_jl=json.dumps(carros_lista)
print(carros_j)
print(carros_jt)
print(carros_lista)

#========#
# AULA 3
#========#
print('aula3')
import json

jogador_j='{"Nome":"Bruno","Time":"aviadores","vivo":"True","Energia":100,"Mochila":["Perdeneira","Corda","Linha","arame"],"aeronaves":[{"Tipo":"Transporte","Habilidade":80},{"Tipo":"ataque","Habilidade":100},{"Tipo":"Reconhecimento","Habilidade":50}]}'

jogador = json.loads(jogador_j)

#chaves
for c in jogador.keys():
    print(c)

#items
for i in jogador.items():
    print(i)

#valores
for v in jogador.values():
    print(v)

#imprimir algo especifico
print(jogador["Nome"])

#imprimir arrays
for im in jogador["Mochila"]:
    print(im)

#imprimir dic dentro de uma lista
for a in jogador["aeronaves"]:
    print(f'{a["Tipo"]} = {a["Habilidade"]}')


#=========#
#aula 4#
#========#

import json

#abrir arquivo json

#informar caminho
#(load) para aquivo externo
with open('informar caminho(C:/caminho') as f:
    jogador=json.load(f)