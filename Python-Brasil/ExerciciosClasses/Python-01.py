"""
Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor 
"""

class Bola():
    def __init__(self, bola, cor):
        self.bola = bola
        self.cor = cor

    def trocarCor(self,cor):
        self.cor = cor
    
    def mostraCor(self):
        print(f'A cor da bola de {self.bola} e {self.cor}')




b = Bola('Futebol', 'Roxa')
b.mostraCor()
b.trocarCor('Amarelo')
b.mostraCor()