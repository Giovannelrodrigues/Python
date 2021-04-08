class NPC: #classe base, super classe
    def __init__(self, nome, time, forca,municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo=True
        self.energia=100

    def info(self):
        print(f'Nome:....{self.nome}')
        print(f'Time:....{self.time}')
        print(f'forca:...{self.forca}')
        print(f'Municao:.{self.municao}')
        print(f'Vivo:....{"Está Vivo"if self.vivo else "Está Morto"}')
        print(f'Energia:.{self.energia}')
        print('=================================')
    
class Soldado(NPC):
    def __init__(self, nome, time):
        self.forca = 20
        self.municao = 100
        super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca = 10
        self.municao = 100
        super().__init__(nome,time,self.forca,self.municao)

class Arqueiro(NPC):
    def __init__(self, nome, time):
        self.forca = 5
        self.municao = 100
        super().__init__(nome,time,self.forca,self.municao)
        def inf(self):
            super().info()

s1=Guarda('Guardin', 'Vermelho')
s2=Soldado('Soldardin','Vermelho')
s3=Arqueiro('Arquerin','Vermelho')

s4=Guarda('EL BRABO', 'Branco')
s5=Soldado('EL COSTINHA','Branco')
s6=Arqueiro('EL RUSHADOR','Branco')

s1.vivo=False
s3.vivo=False
s5.vivo=False

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.info()