"""
Faça um programa para imprimir:

        1
        2   2
        3   3   3
        .....
        n   n   n   n   n   n  ... n
        para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

"""

def num(x):
    for c in range(1, x):
        if c == 1:
            print(c)
        else:
            print(f'{str(c) * c}', end='  ')
            print()



n = int(input('Informe um numero: '))
num(n)
