"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""

def reverterN(n):
    n = (str(n))
    return int(n[::-1])



    




numero = int(input('Digite um numero: '))
print(reverterN(numero))
