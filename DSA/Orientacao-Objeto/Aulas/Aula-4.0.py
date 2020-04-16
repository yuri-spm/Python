#Criando a classe aninal - Super-Classe
class animal():
    def __init__(self):
        print('Animal criado')

    def identif(self):
        print('Animal')

    def comer(self):
        print('Comendo')

#Criando a classe cachorro - Sub-Classe
class cachorro(animal):
    def __init__(self):
        animal.__init__(self)
        print('Objeto cachorro criado')

    def identif(self):
        print('Cachorro')

    def latir(self):
        print('Latir')

#Criando um objeto ( Instanciando a classe)
rex = cachorro()

rex.identif()

rex.comer()

rex.latir()
