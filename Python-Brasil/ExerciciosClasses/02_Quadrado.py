"""
Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área; 
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    


    def getLado(self, lado):
         return self.lado


    def setLado(self, lado):
        self.lado = lado
      
       
    
    def calaculaArea(self):
        return self.lado * self.lado



lado = Quadrado(5)
print(lado.calaculaArea())
lado.setLado(12)
print(lado.calaculaArea())




