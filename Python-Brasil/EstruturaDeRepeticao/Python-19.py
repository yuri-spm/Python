#Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

maior = menor = soma = 0
for c in range(0, 5):
    n = int(input(f'Informe {c + 1}º numero: '))
    if n >=0 and n <= 100:
       soma += n
       if n > maior:
            maior = n
       else:
            menor = n
    else:
        print('Informe um numero de 0 a 100')
print()
print(f'O maior número e: {maior}')
print(f'O menor número e: {menor}')
print(f'A soma dos números e: {soma}')
