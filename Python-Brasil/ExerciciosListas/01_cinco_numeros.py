"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os
"""
listaA = list()
for c in range(0, 5):
    resp = int(input(f'Informe {c+1} numero: '))
    listaA.append(resp)

print(listaA)
