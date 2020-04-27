#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Informe o 1º n: '))
n2 = int(input('Informe o 2º n: '))
n3 = int(input('Informe o 3º n: '))

if n1 > n2 and n1 > n3 and n2 < n3:
    print(f'{n1} e o maior')
    print(f'{n2} e o menor')
elif n2 > n1 and n2 > n3 and n3 < n1:
    print(f'{n2} e o maior')
    print(f'{n3} e o menor')
else:
    print(f'{n3} e o maior')
    print(f'{n1} e o menor')