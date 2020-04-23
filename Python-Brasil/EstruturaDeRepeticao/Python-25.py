"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. 

Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se
a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma
é jovem, adulta ou idosa, conforme a média calculada. 
>>>>>>> 32ade59e1243ef048b0f708a02fcf42c37b55242
"""

lista = list()
n = int(input('Digite a quantidades de pessoas entrevistadas: '))
for c in range(0, n):
    resp = int(input('Digite sua idade: '))
    lista.append(resp)

media = sum(lista)/len(lista)
if media <= 25:
    print('Jovem')
elif media > 26 or media < 60:
    print('Adulto')
else:
    print('Idoso')

    print('Idoso')
