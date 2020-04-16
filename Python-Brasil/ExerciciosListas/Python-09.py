"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

"""


listaA = list()
listaB = list()

for c in range(0, 10):
    resp = int(input(f'Informe {c+1} numero: '))
    listaA.append(resp)
print(listaA)
for d in range(0, 10):
    listaB.append((listaA[d] ** 2))


print(listaB)
