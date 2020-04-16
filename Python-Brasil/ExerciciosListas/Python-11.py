"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""

listaA = list()
listaB = list()
listaC = list()
listaD = list()

for c in range(0, 10):
    resp1 = int(input(f'Informe {c+1}º numero: '))
    listaA.append(resp1)
print()
for d in range(0, 10):
    resp2 = int(input(f'Informe {d+1}º numero: '))
    listaB.append(resp2)

for j in range(0, 10):
    resp3 = int(input(f'Informe {j+1}º numero: '))
    listaB.append(resp3)

print(listaA)
print(listaB)
print(listaC)
for h in range(0, 10):
    listaD.append(listaA[h])
    listaD.append(listaB[h])
    listaD.append(listaC[h])
print()
print(listaD)
