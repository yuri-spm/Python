from datetime import date, datetime

class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} ja esta falando')
            return

        print(f'{self.nome}, esta falando sobre {assunto}')
        self.falando = True


    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não esta falando')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False


    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando.')
            return

        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer.')
        self.comendo = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade



p1 = Pessoa('Joao', 29)
p1.comer('Maça')
p1.comer('Maça')
p1.parar_comer()
p1.parar_comer()
p1.falar('POO')
p1.comer('Maça')
p1.parar_comer()
p1.comer('Pera')
p1.falar('POO2')
print(p1.get_ano_nascimento())