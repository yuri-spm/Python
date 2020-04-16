#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores


maior = menor = soma = 0
for c in range(0,5):
    n = int(input(f'Informe {c+1}º numero: '))
    soma += n
    if n > maior:
        maior = n
    else:
        menor = n

print(maior)
print(menor)
print(soma)
