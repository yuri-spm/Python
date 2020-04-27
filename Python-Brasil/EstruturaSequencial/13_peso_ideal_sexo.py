#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
#    Para homens: (72.7*h) - 58
 #   Para mulheres: (62.1*h) - 44.7


print('     Peso Ideal ')
h = float(input('Informe a altura: '))
while True:
    resp = input('Informe o seu sexo [M / F]: ').upper()
    if resp in 'MF':
        break
    print('Erro, por favor digite M ou F')
if resp == 'M':
    pideal = (70.7 * h) -58
    print(f'O peso ideal para você e: {pideal} ')
else:
    pideal = (60.1 * h) - 44.7
    print(f'O peso ideal para você e: {pideal}')
