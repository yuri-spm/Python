from datetime import date, datetime
from random import randint

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        

    def get_ano_nascimento(self):
        print( self.ano_atual - self.idade)

    
    
    #metodo da classe
    @classmethod 
    def por_ano_nascimento(cls, nome, ano_nascimento):
    #cls refere a classe e não a instance que no caso seria self
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    #não precisa de instancia nem de classe
    #metodo static
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand



p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.idade)
p1.get_ano_nascimento()

print(Pessoa.gera_id())
print()
print(p1.gera_id)
