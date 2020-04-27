#A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,..
#Faça um programa que gere a série até que o valor seja maior que 500.


cont = 0
n1=0
n2=1
while cont != 500:

   n1 += 1
   n2+=n1-1
   print('{} '.format(n2), end=' ')
   cont += 1




