"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""
import math 

def achaTamanho(numero):
    numero = abs(int(numero))
    if numero < 2:
        return 1
    count = 0
    valor = 1
    while valor <= numero:
        valor *= 10
        count += 1
    return count

def achaTamanho2(numero):
    numero = abs(int(numero))
    return (1 if numero == 0 else math.floor(math.log10(numero)) + 1)





print(achaTamanho(8))

