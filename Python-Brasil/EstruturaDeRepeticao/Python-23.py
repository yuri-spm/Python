#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

cont = 0
n = int(input('Digite um número:'))
for c in range (1, n):
    if n % c ==0:
        cont+=1
    
if cont <= 2:
    print(f'O {n} é numero primo')


