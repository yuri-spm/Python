"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;
"""
cont7 = 0
contMaior = 0
contMenor = 0
listaA = list()
resp1 = 0
while resp1 != -1:
    resp1 = int(input('Informe um valor: '))
    if resp1 != -1:
        listaA.append(resp1)

print()
print('-'*20)
print(len(listaA))
for c in range(0, len(listaA)):
    print(listaA[c], end=' ')
print()
print('-'*20)
listaA.reverse()
for d in range(0, len(listaA)):
   print(listaA[d])

print('-'*20)
print(sum(listaA))
print()
print(sum(listaA)/len(listaA))
print('-'*20)
for h in range(0, len(listaA)):
    if listaA[h] > sum(listaA)/len(listaA):
        contMaior += 1
    if listaA[h] < sum(listaA) / len(listaA):
        contMenor += 1
    if listaA[h] < 7:
        cont7 += 1
print(f'Quantidade de numeros acima da média: {contMaior}')
print(f'Quantidade de numeros abaixo da media: {contMenor}')
print(f'Quantidade de numeros menor que sete: {cont7}')