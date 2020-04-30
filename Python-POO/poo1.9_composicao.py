#uma classe e dona de objetos de outra classe.
#se apagar um objeto de uma classe, vai ser apagado da outra.

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))
    

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado





cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Belo Horizando', 'MG')
print(cliente1.nome)
cliente1.lista_endereco()
print()

cliente2 = Cliente('Monica', 32)
cliente2.inserir_endereco('Rio de Janeiro', 'RJ')
cliente2.inserir_endereco('São Paulo', 'SP')
print(cliente2.nome)
cliente2.lista_endereco()
