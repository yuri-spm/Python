#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
#Não utilize a função de potência da linguagem.


while True:
    n1 = int(input('Digite 1º numero: '))
    n2 = int(input('Digite 2º numero: '))
    n3 = n1 ** n2
    resp = input('Para sair digite FIM: ').upper()
    if resp in 'FIM':
        break

print(n3)