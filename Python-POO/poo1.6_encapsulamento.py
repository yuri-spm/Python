"""
metodos e atributos 
public  dentro e fora da classe
protected  apenas dentro da classe ou filhas da classe (herança)
private so esta disponivel dentro da classe

_  -> protected

__  -> privado

"""

class BaseDeDados:
    def __init__(self):
        self.dados = {} #atributo principal publico

    def inserir_clientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else: 
            self.dados['clientes'].update({id: nome})
    
    def lista_cliente(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.dados['clientes'] [id]



bd = BaseDeDados()
bd.inserir_clientes(1, 'Otavio')
bd.inserir_clientes(2, 'Mario')
bd.inserir_clientes(3, 'Bruno')

bd.lista_cliente()
print()
bd.apaga_cliente(2)

bd.lista_cliente()