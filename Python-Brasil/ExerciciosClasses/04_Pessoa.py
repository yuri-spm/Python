"""
Classe Pessoa: Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, 
    a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, 
    ela deve crescer 0,5 cm. 

"""



class Pessoa:
    c = 0
    cont = 0
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura


    def envelhecer(self, idade):
        
        if self.idade < 21:
            idadeantiga = self.idade
            cont = 21 - idadeantiga
            for c in range(0, cont):
                self.altura += 0.5 
        
        self.idade += idade
        

    
    def engordar(self, peso):
        self.peso += peso
           
    
    def emagrecer(self, peso):
        self.peso -= peso
        


    def crescer(self, altura=0):
        self.altura += altura
        

    def imprimeTela(self,):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')




p1 = Pessoa('Yuri', 13, 54, 164)
p1.imprimeTela()
p1.envelhecer(7)
p1.emagrecer(3)
p1.imprimeTela()




    
    