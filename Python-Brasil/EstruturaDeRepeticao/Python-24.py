#Faça um programa que calcule o mostre a média aritmética de N notas.

soma = 0
quant= int(input('Informe a quantidade de notas: '))
for c in range(0, quant):
    n = float(input('Digite a primeira nota: '))
    soma +=n

<<<<<<< HEAD
soma = 0
quant= int(input('Informe a quantidade de notas: '))
for c in range(0, quant):
    n = float(input('Digite a primeira nota: '))
    soma +=n

=======
>>>>>>> 32ade59e1243ef048b0f708a02fcf42c37b55242
print(f'A media das notas foi {(soma/quant):.1f}')