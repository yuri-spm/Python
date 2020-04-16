"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""

listAltura = []
listIdade = []
contIdade = 0
contAltura = 0

for c in range(0, 10):
    resp1 = int(input(f'Informe a idade do {c+1}º aluno: '))
    listIdade.append(resp1)
    resp2 = float(input(f'Informe a altura do {c+1}º aluno: '))
    listAltura.append(resp2)

for i in range(0, 10):
    if listIdade[i] > 13:
       contIdade += 1
    if listAltura[i] > sum(listAltura)/3:
        contAltura += 1



print(f'A quantidade de alunos com altura acima da média é : {contAltura}')
print(f'A quantidade de alunos com idade acima de 13 anos é : {contIdade}')