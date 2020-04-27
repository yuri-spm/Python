"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""


data = input('Informe uma data com dia, mes e ano ex: 10/09/1991: ')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])
print(dia, mes, ano)

if dia >= 1 and dia <= 31:
    print('O dia e valido')
    if mes >= 1 and mes <= 12:
        print('O mes e valido')
        if ano > 0:
            print('O mes e valido')

