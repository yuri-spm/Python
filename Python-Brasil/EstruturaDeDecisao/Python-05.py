"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
soma = (n1 + n2) / 2
if soma < 7:
    print('Reprovado')
elif soma >= 7 and soma <= 9:
    print(('Aprovado'))
elif soma == 10:
    print('Aprovado com Distinçao')

