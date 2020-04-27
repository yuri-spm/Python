"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

listaA = list()

for c in range(0, 10):
    resp = int(input(f'Informe {c+1} numero: '))
    listaA.append(resp)
listaA.reverse()
print(listaA)

