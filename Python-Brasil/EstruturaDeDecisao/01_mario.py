#Faça um Programa que peça dois números e imprima o maior deles.


n1 = int(input('Informe 1º numero: '))
n2 = int(input('Informe 2º numero: '))

if n1 > n2:
    maior = n1
    menor = n2
    print(f'O maior e {maior} e o menor e {menor}')
elif n1 < n2:
    maior = n2
    menor = n1
    print(f'O maior e {maior} e o menor e {menor}')
else:
    print('Os numeros são iguais.')