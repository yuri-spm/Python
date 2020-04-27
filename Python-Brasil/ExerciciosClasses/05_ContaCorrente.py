"""
Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
 A classe deve possuir os seguintes atributos: número da conta, nome do correntista
 e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
 No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios. 
"""



class ContaCorrente:
    def __init__(self, conta, nome, saldo):
        self.nconta= conta
        self.nome = nome
        self.saldo = saldo

    
    def alterarNome(self,conta, nome):
        if conta == self.nconta:
            self.nome = nome
        else:
            print('Conta errada. Por favor informe a conta certa')


    
    def deposito(self, valor):
        self.saldo += valor


    def saque(self, valor):
        self.saldo -= valor

    

    

client1 = ContaCorrente(875468,'Antonio Vasques', 5000)
print(client1.nome)
client1.alterarNome(875468, 'Yuri Santos')
print()
print(client1.nome)
client1.saque(2500)
print (client1.saldo)



