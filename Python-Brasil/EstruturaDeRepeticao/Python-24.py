#Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
quant= int(input('Informe a quantidade de notas: '))
for c in range(0, quant):
    n = float(input('Digite a primeira nota: '))
    soma +=n


soma = 0
quant= int(input('Informe a quantidade de notas: '))
for c in range(0, quant):
    n = float(input('Digite a primeira nota: '))
    soma +=n


print(f'A media das notas foi {(soma/quant):.1f}')
