"""

Um posto está vendendo combustíveis com a seguinte tabela de descontos:

    Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
    Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o
    tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago
    pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

<<<<<<< HEAD

=======
>>>>>>> 8a690647c7dfadec9dde21f72d8b7227561dddd6
resp = int(input('ESCOLHA: \n1 - Alcool \n2 - Gasolina \nOpção:'))


if resp == 1:
    qlitros = int(input('Informe a quantidade de litros: '))
    if qlitros <= 20:
        tlitros = qlitros * 1.9 
        tlitros = tlitros - (tlitros *3/100)
        print(f'TOTAL: {tlitros:.2f}')
    else:
        tlitros = qlitros * 1.9  
        tlitros = tlitros - (tlitros *5/100)
        print(f'TOTAL: {tlitros:.2f}')
        tlitros = qlitros * 1.9
elif resp == 2:
    qlitros = int(input('Informe a quantidade de litros: '))
    if qlitros <= 20:
        tlitros = qlitros * 2.5
        tlitros = tlitros - (tlitros *4/100)
        print(f'TOTAL: {tlitros:.2f}')
    else:
        tlitros = qlitros * 2.5
        tlitros = tlitros - (tlitros * 6/100)
        print(f'TOTAL: {tlitros:.2f}')