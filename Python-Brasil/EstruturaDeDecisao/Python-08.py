#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

n1 = int(input('Informe o valor 1º produto: '))
n2 = int(input('Informe o valor 2º produto: '))
n3 = int(input('Informe o valor 3º produto: '))

if n1 > n2 and n1 > n3 and n2 < n3:
    print(f'{n2} e o menor')
elif n2 > n1 and n2 > n3 and n3 < n1:
    print(f'{n3} e o menor')
else:
    print(f'{n1} e o menor')