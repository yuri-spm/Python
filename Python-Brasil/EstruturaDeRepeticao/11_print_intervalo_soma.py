#Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input('Informe 1º numero: '))
n2 = int(input(('Informe 2 numero: ')))
soma = 0
for c in range(n1+1, n2):
    soma += c
print(soma)
