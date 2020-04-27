"""Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento.
 Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

 Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

 """

resp1 = input('Digite a primeira frase: ')
resp2 = input(('Digite a segunda frase: '))
print(f'{resp1} : {len(resp1)} caracteres')
print(f'{resp2} : {len(resp2)} carateres')
if len(resp1) != len(resp2):
    print('As duas strings são de tamanhos diferentes')
else:
    print('As duas strings são de tamanhos de iguais')
if resp1 == resp2:
    print('As duas strings tem o mesmo conteudo')
else:
    print('As duas strings tem o conteudo diferente')