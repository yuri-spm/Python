#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

contP = 0
contI = 0

for c in range(1, 21):
    n1 = int(input('Informe um numero: '))
    if n1 % 2 == 0:
        contP += 1
    else:
        contI += 1
print(f'Total de numero par {contP}')
print(f'Total de numero impar {contI}')