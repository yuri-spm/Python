"""

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
"""
n1 = int(input('Informe um numero: '))
n1 = str(n1)

if n1[0] != 0 and len(n1) == 3:
    print(f'{n1[0]} centenas')
    print(f'{n1[1]} dezenas')
    print(f'{n1[2]} unidades')

elif n1[0] != 0 and len(n1) == 2:
    print(f'{n1[0]} dezenas')
    print(f'{n1[1]} unidades')

else:
    print(f'{n1[0]} unidades')
"""
n1 = str(int(input('Informe um numero: ')))

if len(n1) == 3:
    print(f'{n1[2]} centenas')

if len(n1) >= 2:
    print(f'{n1[1]} dezenas')

print(f'{n1[0]} unidades')

