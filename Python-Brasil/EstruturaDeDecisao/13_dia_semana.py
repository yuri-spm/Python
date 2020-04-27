"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

"""
print(' 1 - DOMINGO\n 2 - SEGUNDA \n 3 - TERÇA \n 4 - QUARTA \n 5 - QUINTA  \n 6 - SEXTA')

resp = int(input('Informe o número: '))
if resp == 1:
    print('Domingo')
elif resp == 2:
    print('Segunda')
elif resp == 3:
    print('Terça')
elif resp == 4:
    print('Quarta')
elif resp == 5:
    print('Quinta')
if resp == 6:
    print('Sexta')
else:
    print('Numero INVALIDO')
    