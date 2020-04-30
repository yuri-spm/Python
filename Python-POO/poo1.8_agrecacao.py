# Uma classe usa outra classe por parte de si, e uma classe precisa da outra, um não funciona sem o outro

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []


    def inserir_produtos(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)


    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta',50)
p2 = Produto('iPhone',2500)
p3 = Produto('Caneca',30)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.lista_produtos()
print(carrinho.soma_total())