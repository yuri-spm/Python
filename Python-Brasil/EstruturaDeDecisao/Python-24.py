"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.

"""

valor = float(input('Informe um numero: '))

print ('1 - Par ou Impar')
print ('2 - Positivo ou Negativo')
print ('3 - Inteiro ou Decimal')
opcao = (input('Escolha uma opcao: '))

if (opcao == '1'):
    if (valor % 2 == 0):
        print ('Valor eh par')
    else:
        print ('Valor eh impar')
elif (opcao == '2'):
    if (valor < 0):
        print ('Valor eh negativo')
    elif (valor > 0):
        print ('Valor eh positivo')
    else:
        print ('Valor eh igual a zero')
elif (opcao == '3'):
    if (valor == int(valor)):
        print ('Valor eh inteiro')
    else:
        print ('Valor eh decimal')
else:
    print ('Opcao Invalida')