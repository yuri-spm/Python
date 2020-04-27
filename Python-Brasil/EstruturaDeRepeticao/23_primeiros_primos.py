#Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
#O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
#Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input("Verificar numeros primos ate: "))
cont =0

for c in range(1,n):
    if (n % c == 0):
       cont += 1 

if(cont < 2):
    print(f"{n} É primo")
else:
    print(f"Tem {cont} múltiplos acima de 2 e abaixo de {n}")

