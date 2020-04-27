"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 
"""

l1 = float(input('Infomer o primeiro lado do triangulo em metros: '))
l2 = float(input('Informe o segundo lado do  triangulo em metros: '))
l3 = float(input('Informe o terceiro lado do triangulo em metros: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 == l2 and l2 == l3:
   print('Ok, suas medidas formam um triangulo EQUILATERO')

elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 != l2 and l2 != l3 and l1 != l3:
   print('Ok, suas medidas formam um triangulo  ESCALENO.')
elif l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2 and l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2:
   print('Ok, suas medidas formam um triangulo ISOCELES.')
else:
   print("Suas medidas nao formam um triangulo.")