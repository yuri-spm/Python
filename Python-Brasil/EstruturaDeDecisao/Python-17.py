"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

"""

ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print('O ano {} é BISSEXTO'.format(ano))
else:
   print('O ano {} NÃO E BISSEXTO'.format(ano))