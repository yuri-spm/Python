"""

Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    F
    U
    L
    A
    N
    O

"""
resp = input('Informe seu nome:')
for c in range(0, len(resp)):
    print(resp[c])