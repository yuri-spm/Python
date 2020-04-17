#Criando uma classe
class Estudantes:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

estudante1 = Estudantes('Yuri', 28, 10)
print(estudante1.nome)
print(estudante1.idade)
print(estudante1.nota)