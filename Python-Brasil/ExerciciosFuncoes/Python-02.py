"""
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def num(x):
    for c in range(1, x):
        if c == 1:
            print(c)
        else:
            print(f'{str(c) * c}', end='  ')
            print()


