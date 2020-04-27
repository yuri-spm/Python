"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o 
valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. 

"""
total = 0
n = int(input('Informe a quantidade de cd(s):' ))
for c in range(0, n):
    resp=float(input(f'Valor do {c+1}º cd: '))
    total += resp

total = total / n
print(f'A media investida em cd(s): {total}')
