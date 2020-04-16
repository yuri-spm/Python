#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for c in range(0, 5):
    n = int(input('Informe o numero:'))
    soma += n

media = soma / 5
print(f'A soma e {soma} e a media e {media}' )
