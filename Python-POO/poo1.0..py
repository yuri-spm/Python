# Class
# Sintaxe
# self serve para vc acessar as propriedades ou metodos
# Marca, Memoria Ram, Placa de video

class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print('Ligando')


    def desligar(self):
        print('Desligando')

    
    def exibirInformacoes(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = Computador('Asus', '16gb', 'Nvidia')
computador1.ligar()
computador1.exibirInformacoes()
computador1.desligar()