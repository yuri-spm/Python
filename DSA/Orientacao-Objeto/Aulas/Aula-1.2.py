class Livro():
    def __init__(self):
        self.titulo = "O monge e o Executivo"
        self.isbn = 9988888
        print('Construtor chamado para criar um ojeto desta classe')

    def imprime(self):
        print(f'Foi criado o livro {self.titulo} e {self.isbn} ')



livro1 = Livro()
print(type(livro1))
print(livro1.titulo)
livro1.imprime()

