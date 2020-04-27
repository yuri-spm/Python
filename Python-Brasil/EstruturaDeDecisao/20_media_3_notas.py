"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
soma = (n1 + n2 + n3) / 3
if soma < 7:
    print('Reprovado')
elif soma >= 7 and soma <= 9:
    print(('Aprovado'))
elif soma == 10:
    print('Aprovado com Distinçao')
