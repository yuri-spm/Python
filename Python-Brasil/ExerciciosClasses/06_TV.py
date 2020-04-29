"""
Classe TV: Faça um programa que simule um televisor criando-o como um objeto.
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. 
Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas. 
"""

class Tv:
    def __init__(self,canal,volume=0):
        self.canal = canal
        self.volume = volume
        

    
    def volumeMax(self, volume):
        self.volume += volume
        return volume

    def volumeMin(self, volume):
        self.volume -= volume
        return volume
    
    def verificaVolumeMax(self, volume):
        if self.volume <= 100:
            print('O volume esta no máximo')

    

    
   

tv1 = Tv(4,50)
print(tv1.volume)
tv1.volumeMax(60)
print(tv1.volume)
