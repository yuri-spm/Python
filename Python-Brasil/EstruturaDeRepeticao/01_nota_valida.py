"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.
"""

while True:
    n1 = int(input('Informe um numero entre 0 e 10: '))
    if n1 < 0 or n1 > 10:
        print('Nota invalida')
        break
    else:
        continue