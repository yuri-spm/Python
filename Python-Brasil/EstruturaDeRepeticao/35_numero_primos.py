"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um 
número inteiro informado pelo usuário. 
"""


n = int(input("Verificar numeros primos ate: "))
cont =0

for c in range(1,n):
    if (n % c == 0):
       cont += 1 

if(cont < 2):
    print(f"{n} É primo")
else:
    print(f"Tem {cont} múltiplos acima de 2 e abaixo de {n}")