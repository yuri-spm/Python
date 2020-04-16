#Faça um Programa que pergunte quanto você ganha por hora e o número de
# horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.


salHora = float(input("Informe quanto vc ganha por hora: "))
hora = int(input("Quantas horas trabalhadas: "))
salTotal = (salHora * hora) * 30
print(salTotal)