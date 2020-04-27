#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#  C = (5 * (F-32) / 9).

f = int(input('Informe a temperatura em Fª: '))

c = (5 * (f-32) / 9 )

print(f'{c:.0f}ºC')