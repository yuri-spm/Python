"""
Classe Retangulo: Crie uma classe que modele um retangulo:

    Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
    Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades
     de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de
      rodapés necessárias para o local. 


"""




class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def setmudarValores(self, base, altura):
        self.base = base
        self.altura = altura
    
    def getmostrarValores(self, base, altura):
        print(f'A base e {self.base} e altura {self.altura}')
    
    def calculaArea(self):
        return self.base * self.altura



retangulo = Retangulo(4, 10)
print(retangulo.calculaArea())
retangulo.setmudarValores(20, 35)
print(retangulo.calculaArea())




