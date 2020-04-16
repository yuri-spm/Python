"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

par = list()
impar = list()

for c in range(0, 20):
    resp = int(input(f'Informe {c+1}° número: '))
    if resp % 2 == 0:
        par.append(resp)
    else:
        impar.append(resp)
print(f'Pares: {par}')
print(f'Impares: {impar}')