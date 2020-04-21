"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
    Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
     5 como "Assassino". Caso contrário, ele será classificado como "Inocente".



"""

cont = 0
print('RESPONDA SIM OU NÃO'.center(50))
resp = input('Telefonou para vitima: ').upper()
if resp in "SIM":
    cont+= 1
resp = input('Esteve no local do crime: ').upper()
if resp in "SIM":
    cont+= 1
resp = input('Nora perto da vitima: ').upper()
if resp in "SIM":
    cont+= 1
resp = input('Devia para vitima: ').upper()
if resp in "SIM":
    cont+= 1
resp = input('Já trabalhou para vitima: ').upper()


if resp in "SIM":
    cont+= 1
if cont == 2:
    print('Você e suspeita.') 
elif cont == 3 or cont == 4:
    print('Cumplice')

elif cont == 5 :
    print('Culpada')
else:
    print('Inocente')