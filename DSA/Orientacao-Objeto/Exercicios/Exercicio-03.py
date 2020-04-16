# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2
# métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos
# especiais
class Pessoa():

    def __init__(self, nome, cidade, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.email = email
        print("Cadastrado com sucesso")

    def print_info(self):
        print(f'O seu nome e {self.nome}, o local que você mora e {self.cidade}')
    def __str__(self):
        return "O usuário " + self.nome + " mora na cidade " + self.cidade

p = Pessoa('Yuri','Rio de Janeiro',212345678,'teste@teste.com')
p.print_info()
print(p.telefone)
str(p)