#escrever == exemplo do diretório
arquivo = open('C:temp/Python/CEV/OutrasAulas/Teste', 'w')
arquivo.write('Minha primeira escrita\n')
arquivo.write('Segunda Linha\n')
arquivo.close()
#atualizar
arquivo = open('Teste', 'a')
arquivo.write('Minha primeira escrita\n')
arquivo.write('Segunda Linha\n')
arquivo.close()

#fun
def escrever(txt):
    arquivo = open('Teste', 'w')
    arquivo.write(txt)
    arquivo.close()

def atualizar(txt):
    arquivo = open('Teste', 'a')
    arquivo.write(txt)
    arquivo.close()

def ler(arquivo):
    arq = open(arquivo, 'r')
    txt = arq.read()
    print(txt)

def copia(arquivo):
    import shutil
    shutil.copy(arquivo, '#DIRETÓRIO')

def move(arquivo):
    import shutil
    shutil.move(arquivo, '#DIRETÓRIO')