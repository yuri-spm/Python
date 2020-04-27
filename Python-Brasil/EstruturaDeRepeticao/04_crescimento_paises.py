"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número
de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

"""

cont = 0
a = 80000
b = 200000
crescA = 1.03
crescB = 1.015
while a < b:
    a *= crescA
    b *= crescB
    cont += 1

print(f'Serão necessarios  {cont} anos, para que o país A passe o país B')