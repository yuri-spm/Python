#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

n = int(input('Informe um numero: '))
f = 1
for c in range(n, 0, -1):
    f *= c
    print(c, end=' ')
    if c > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
print(f, end=' ')



