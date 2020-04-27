"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
 programa que calculará os reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""

sal = float(input('Informe seu salario: '))
if sal <= 280:
    salario = sal + (sal *20/100)
    print(f'Seu salario {sal}')
    print(f'Aumento proposto 20%')
    print(f'Salario ajustado {salario}')

elif sal > 280 and sal <= 700:
    salario  = sal + (sal * 15/100)
    print(f'Seu salario {sal}')
    print(f'Aumento proposto 15%')
    print(f'Salario ajustado {salario}')
elif sal > 700 and sal <= 1500:
    salario = sal + (sal * 10/100)
    print(f'Seu salario {sal}')
    print(f'Aumento proposto 20%')
    print(f'Salario ajustado {salario}')
else:
    if sal > 1500:
        salario = sal + (sal * 5/100)
        print(f'Seu salario {sal}')
        print(f'Aumento proposto 5%')
        print(f'Salario ajustado {salario}')