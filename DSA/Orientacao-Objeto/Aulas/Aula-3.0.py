#Criando uma classe chamada circulo
class circulo():
    #O valor de po é constante
    pi = 3.14

    #Quando um ojeto desta classe for criado, este método será executado e o valor default do raio será 5.
    def __init__(self, raio=5):
        self.raio = raio

    #Esse método calcula a área. Self utiliza os atributos desde mesmo objeto
    def area(self):
        return (self.raio * self.raio) * circulo.pi

    #Método para gerar um novo raio
    def setRaio(self, novo_raio):
        self.raio = novo_raio


    #Método para obter o raio do círculo
    def getRaio(self):
        return self.raio


#Executando  um método da classe circulo
circ = circulo()
#Resultado da execução
print(circ.getRaio())
#Executando o método com parâmetro
circ1 = circulo(7)
print(circ1.getRaio())


#Imprime o raio
print(f'O raio é: {circ1.getRaio()}')


#Imprime a área
print(f'A área é: {circ1.area()}')

#Gerando um novo valor para o raio do círculo
circ.setRaio(3)

#Imprimindo novo raio
print(f'O novo raio e igual a: {circ.getRaio()}')
