#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial
# a números inteiros positivos e menores que 16.

while True:
    print('Infome números entre 0 e 16')
    n = int(input('Informe um numero: '))
    if n > 0 and n < 16:
        f = 1
        for c in range(n, 0, -1):
            f *= c
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        print(f, end=' ')
    else:
        print('Número fora do padrão!!!')
        print()