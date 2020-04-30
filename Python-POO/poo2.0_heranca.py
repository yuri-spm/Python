# Associacao - USA | Agregacao - TEM  | Composicao - DONO | Herenca - É

#heranca funciona de cima para baixo

#subclasse
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


    def falar(self):
        print(f'{self.nomeclasse} esta falando ..')

#classefilha
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} esta comprando ..')

class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} esta estudando ..')



c1 = Cliente('Luiz', 45)
print(c1.nome)
a1 = Aluno('Maria', 54)
print(a1.nome)
a1.falar()
c1.falar()
a1.estudar()
#a1.comprar()