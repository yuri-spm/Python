class Carro:
    def __init__(self, marca, ano, ligado=False, andando=False):
        self.marca = marca
        self.ano = ano
        self.ligado = ligado
        self.andando = andando


    def ligar(self):    
        if self.ligado:
            print('Ja esta ligado')
            return

        print('O carro esta ligando')
        self.ligado = True

    def desligar_carro(self):
        if not self.ligado:
            print('O carro ja esta desligado')
            return
        print('Desligando o carro')
        self.ligado = False

    def andar(self):
        if not self.ligado:
            print('Ligue o carro')
            return

        if self.andando:
            print('O carro já esta andando!')
            return    
        
        print('Carro andando...')
        self.andando = True
                
    def parar_andar(self):
        if not self.andando:
            print('O carro ja esta parado.')
            return
        print('Parando o carro')
        self.andando = False


c1 = Carro('Chevrole', 2002)
c1.ligar()
c1.ligar()
c1.desligar_carro()
c1.desligar_carro()
c1.andar()
c1.ligar()
c1.andar()
c1.andar()
c1.parar_andar()
c1.parar_andar()
c1.ligar()
c1.andar()
