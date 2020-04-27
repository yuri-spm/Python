"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vogais = ['A', 'E', 'I', 'O', 'U']
consoante = list()
letra = list()
for c in range(0, 10):
    resp = input('Digite uma letra: ').upper()
    letra.append(resp)

for i in range(0, 10):
    if letra[i] not in vogais:
        consoante.append(letra[i])
print(consoante)
print(f'Total de consoantes digitadas: {len(consoante)}')
