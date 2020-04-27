"""

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
 quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é
 de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de
    5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas
    de 10, uma nota de 5 e quatro notas de 1.

"""

cont50 = 0
cont20 = 0
cont10 = 0
cedula50 = 0
cedula20 = 0
cedula10 = 0
print('-'*50)
print('BEM VINDO AO NUBANK')
print('-'*50)
while True:
    salario = int(input('Valor a ser sacado:'))
    if salario > 50 :
        cedula50 = salario // 50
        salario = ( salario % 50)
    if salario > 20:
        cedula20 = salario  // 20
        salario =  (salario % 20)
    if salario % 10 == 0:
        cedula10 = (salario // 10)
    break
if cedula50 != 0:
    print('{:.1f} nota(s) de 50 reais'.format(cedula50))
if cedula20 != 0:
    print('{:.1f} nota(s) de 20 reais'.format(cedula20))
if cedula10 != 0:
    print('{:.1f} nota(s) de 10 reais'.format(cedula10))


print('-'*50)
print('FINALIZANDO')
print('-'*50)
