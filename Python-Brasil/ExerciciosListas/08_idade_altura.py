"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""


altura = list()
idade = list()

for c in range(0, 2):
    resp1 = int(input('Informe a sua idade: '))
    idade.append(resp1)
    resp2 = float(input('Informe a sua altura: '))
    altura.append(resp2)

print(sorted(idade, reverse = True))
print(sorted(altura, reverse = True))