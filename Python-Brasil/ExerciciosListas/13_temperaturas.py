"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""


print('1- Janeiro, 2 - Fevereiro, 3 - Março, 4 - Abril, 5 - Maio, 6 - Junho, 7 - Julho, 8 - Agosto, 9 - Setembro, 10 - Outubro,'
      '11 - Novembro, 12 - Dezembro')

listaM = list()

print('Informe a temperatura de cada mês.')
for c in range(0, 12):
    resp = int(input(f'{c+1}º mês: '))
    listaM.append(resp)

for d in range(0, 12):
    if listaM[d] > sum(listaM)/12:

        print(f'Temperaduras acima da média:{d+1}º mês temperatura {listaM[d]} ')
print()
print(f'A media anual foi: {sum(listaM)/12} ')