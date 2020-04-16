# Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface e crie a classe MP3Player com os 
# atributos capacidade. A classe MP3player deve herdar os atributos da classe Smartphone.

class smartphone():
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        print('Criado com sucesso')
    
class mp3Player(smartphone):
    def __init__(self, capacidade, corled='verde'):
        self.capacidade = capacidade
        self.corled = corled
        smartphone.__init__(self, tamanho='tela7', interface='led')
        print('Cadastrado com sucesso')
    def print_mp3player(self):
        print(f'Objeto criado {self.tamanho}, {self.corled} e a {self.interface}')

aparelho = smartphone('tela9','Amoled')
aparelho = mp3Player('128 GB', 'Azul')
aparelho.print_mp3player()