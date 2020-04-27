"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. 
A saída deve ser conforme o exemplo abaixo:

    Fatorial de: 5
    5! =  5 . 4 . 3 . 2 . 1 = 120
"""


n = int(input('Digite um numero para ver seu fatoria: '))
print(f'Fatorial de: {n}')
total = 1
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    total *= c
    if c != 1:
        print(f'{c}.', end=' ')
    else:
        print(f'{c} = {total}', end=' ')