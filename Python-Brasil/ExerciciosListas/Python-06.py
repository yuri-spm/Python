"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
"""
soma = 0
media = 0
notas = list()
for c in range(0, 10):
    for a in range(0, 4):
        resp = float(input(f'Informe a nota do {c+1}° aluno: '))
        if resp >= 0 and resp <= 10:
            soma += resp

    media = soma/4
    notas.append(media)
    media = 0
    soma = 0

for n, m in enumerate(notas):
    if m >= 7:
        print(f'O {n+1}º aluno tirou a nota: {m} e esta aprovado.')
    else:
        print(f'O {n+1}º aluno tirou a nota: {m} e esta reprovado.')
