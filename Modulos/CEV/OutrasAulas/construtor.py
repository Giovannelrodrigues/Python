class Carro:
    velMax=0
    ligado=False
    cor=''

    def __init__(self, v, l, c):
        self.velMax = v
        self.ligado = l
        self.cor = c

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def andar(self):
        if(self.ligado):
            print('Andando....')
        else:
            print('Parado....')


    def mostrar(self):
        if self.ligado == True:
            estado = 'ligado'
        else:
            estado = 'Desligado'
    
        print(f'Velocidade maxima:.... {self.velMax}')
        print(f'Ligado ou Desligado:.. {estado}')
        print(f'Cor:.................. {self.cor}')
        print(f'===============================')
    


c1=Carro(200,False,'Prata')
c2=Carro(220,False,'Branco')
c3=Carro(150,False,'Vermelho')

c1.ligar()
c1.mostrar()
c2.ligar()
c2.mostrar()
c3.ligar()
c3.andar()
c3.mostrar()
c1.andar()
c2.andar()
c3.andar()