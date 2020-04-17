# Criando uma classe chamada Livro
class Livro():
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe

    def __init__(self, titulo, isbn):
        # Atributos de cada objeto criado a partir desta classe.
        # O self indica que estes são atributos dos objetos

        self.titulo = titulo
        self.isbn = isbn

    # Métodos são funções, que recebem como parâmetro atributos do objeto criado
    def imprime(self, titulo, isbn):
        print(f'Este livro {titulo} e {isbn}')

livro2 = Livro('A Menina que Roubava Livros', 77886611)
print(livro2.titulo)
livro2.imprime('A Meninna que Roubava Livros',77886611)


