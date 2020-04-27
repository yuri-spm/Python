#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

c = int(input('Informe a temperatura em ºC: '))
f = c * (9/5) + 32
print(f'{f:.0f}')