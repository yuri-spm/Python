#Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Informe o 1º n: '))
n2 = int(input('Informe o 2º n: '))
n3 = int(input('Informe o 3º n: '))

if n1 > n2 and n1 > n3:
    print(f'{n1} e o maior')
elif n2 > n1 and n2 > n3:
    print(f'{n2} e o maior')
else:
    print(f'{n3} e o maior')