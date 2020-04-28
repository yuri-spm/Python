"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

    Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
    Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
    A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 
    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
    que o usuário digite o salário inicial do funcionário. 
"""


from datetime import date

anoFinal = date.today().year
print(anoFinal)

ano = 1995
salario = 1000
r = 1.5

while (ano <= anoFinal):
    print(f'Ano {ano} teve um reajuste de {r} e o valor passou a ser {salario:.2f}')
    salario += (salario * (r /100))
    ano +=1
    r *= 2



