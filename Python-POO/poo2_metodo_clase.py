from datetime import date, datetime

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


p1 = Pessoa.por_ano_nascimento('Luiz', 1987)
print(p1.idade)
p1.get_ano_nascimento()