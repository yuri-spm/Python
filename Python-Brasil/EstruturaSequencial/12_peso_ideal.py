#Tendo como dados de entrada a altura
# de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (70.7*altura) - 58

print('     Peso Ideal ')
h = float(input('Informe a altura: '))
pideal = (70.7 * h) -58
print(f'O peso ideal para você e: {pideal:.2f}')
