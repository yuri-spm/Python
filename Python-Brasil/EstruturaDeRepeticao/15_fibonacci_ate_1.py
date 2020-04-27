#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.


cont = 0
n1=0
n2=1
while cont != 10:

   n1 += 1
   n2+=n1-1
   print('{} '.format(n2), end=' ')
   cont += 1


termos = int(input('\nQuantos termos você quer mostrar? '))
cont = 0
t1 = 0
t2 = 1
while cont < termos:
   print(t1, end=' ')
   t1 = t1 + t2
   t2 = t1 - t2
   cont += 1

