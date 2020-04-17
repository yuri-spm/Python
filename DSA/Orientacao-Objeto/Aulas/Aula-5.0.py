# Criando a classe Livro
class Livro():
    def __init__(self, titulo, autor, paginas):
        print("Livro criado")
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return "Título: %s , autor: %s, páginas: %s " \
               % (self.titulo, self.autor, self.paginas)

    def __len__(self):
        return self.paginas

    def len(self):
        return print("Páginas do livro com método comum: ", self.paginas)



livro1 = Livro('Os Lusíadas', 'Luis de Camões', 8816)
print(livro1)
str(livro1)
print(len(livro1))
livro1.len()
del livro1.paginas
print(hasattr(livro1, "paginas"))

