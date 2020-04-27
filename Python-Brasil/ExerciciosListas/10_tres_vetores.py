"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""

listaA = list()
listaB = list()
listaC = list()

for c in range(0, 10):
    resp1 = int(input(f'Informe {c+1}º numero: '))
    listaA.append(resp1)
print()
for d in range(0, 10):
    resp2 = int(input(f'Informe {d+1}º numero: '))
    listaB.append(resp2)

print(listaA)
print(listaB)

for h in range(0, 10):
    listaC.append(listaA[h])
    listaC.append(listaB[h])
print()
print(listaC)
