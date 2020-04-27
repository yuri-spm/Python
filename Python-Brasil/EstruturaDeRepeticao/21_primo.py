#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

cont = 0
n1 = int(input('Digite um número:'))
for c in range (1, n1):
 if n1 % c ==0:
   cont+=1
if cont <= 2:
 print(f'O {n1} é numero primo')
else:
 print(f'O {n1}  não e  um primo')