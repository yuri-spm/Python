#uma classe não depende da outra


class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    
    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

class Caneta:
    def __init__(self, marca):
        self.__marca = marca
    
    @property
    def marca(self):
        return self.__marca
    
    def escrevrer(self):
        print('Caneta esta escrevendo...')

class MaquinaDeEscrever:
    def escrever(self):
        print('Maquina escrevendo..')






escritor = Escritor('Joao')
caneta = Caneta('Bic')
print(caneta.marca)
maquina = MaquinaDeEscrever()

print('Associação')

escritor.ferramenta = maquina
escritor.ferramenta.escrever()
