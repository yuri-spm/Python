"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
soma = 0
notas = list()
for c in range(0, 4):
    resp = float(input(f'Informe {c+1}º nota do aluno: '))
    soma += resp
    notas.append(resp)

media = soma /4
print(f'As notas foram {notas}')
print(f'A media foi: {media}')