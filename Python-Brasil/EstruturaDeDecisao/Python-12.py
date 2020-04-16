"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11%
do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário
 Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

    Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.


"""

sal = float(input('Informe o salário: '))
if sal <= 900:
    inss = sal * (8/100)
    sind = sal * (3/100)
    #ir = sal * (11/100)
    fgts = sal * (11 / 100)
    salLiquido = ((sal - inss) - sind) -fgts
    tDESCONTO = inss + sind + fgts
    print(f'Salário bruto:  {sal}')
    print(f'INSS:           {inss:.2f}')
    print(f'Sindicato:      {sind:.2f}')
    print('IR:             ISENTO')
    print((f'FTGS            {fgts:.2f}'))
    print(f'Total desconto  {tDESCONTO}')
    print()
    print(f'Salário liquido: {salLiquido:.2f}  ')
elif sal >= 900 and sal < 1500:

    inss = sal * (8 / 100)
    sind = sal * (3 / 100)
    ir = sal * (5/100)
    fgts = sal * (11 / 100)
    salLiquido = (((sal - inss) - sind) -ir)-fgts
    tDESCONTO = inss + sind + fgts
    print(f'Salário bruto:  {sal}')
    print(f'INSS:           {inss:.2f}')
    print(f'Sindicato:      {sind:.2f}')
    print(f'IR:             {ir:.2f}')
    print((f'FTGS            {fgts:.2f}'))
    print(f'Total desconto  {tDESCONTO}')
    print()
    print(f'Salário liquido: {salLiquido:.2f}  ')
elif sal >= 1500 and sal < 2500:
    inss = sal * (8 / 100)
    sind = sal * (3 / 100)
    ir = sal * (10/100)
    fgts = sal * (11/100)
    salLiquido = (((sal - inss) - sind) - ir) - fgts
    tDESCONTO = inss + sind + fgts
    print(f'Salário bruto:  {sal}')
    print(f'INSS:           {inss:.2f}')
    print(f'Sindicato:      {sind:.2f}')
    print(f'IR:             {ir:.2f} ')
    print(f'FGTS            {fgts:.2f} ')
    print((f'FTGS            {fgts:.2f}'))
    print(f'Total desconto  {tDESCONTO:.2f}')
    print()
    print(f'Salário liquido: {salLiquido:.2f}  ')
else:
    if sal >= 2500:
        inss = sal * (8 / 100)
        sind = sal * (3 / 100)
        ir = sal * (20 / 100)
        fgts = sal * (11/100)
        salLiquido = ((sal - inss) - sind) - ir
        tDESCONTO = inss + sind + fgts
        print(f'Salário bruto:  {sal}')
        print(f'INSS:           {inss:.2f}')
        print(f'Sindicato:      {sind:.2f}')
        print(f'IR:             {ir:.2f} ')
        print((f'FTGS            {fgts:.2f}'))
        print(f'Total desconto  {tDESCONTO}')
        print()
        print(f'Salário liquido: {salLiquido:.2f}  ')
