#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

cont = 0
n1 = int(input('Digite um número: '))
for c in range(1, n1):
 if n1 % c ==0:
   cont+=1
if cont <= 2:
 print(f'O {n1} é numero primo')
else:
 print(f'O {n1}  não e  um primo')
 for c in range(1, n1):
    if n1 % c != 0:
        print(f'{c} ', end='')