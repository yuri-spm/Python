"""
Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd'; 
"""

nome = ''
idade = -1
sal = -1
sexo = ''
estado_civil ='A'
while len(nome) < 3:
    nome = input('Infome seu nome: ')
    if len(nome) <= 3:
        print('Nome tem que ser maior.')
while idade < 0 or idade > 150:
    idade = int(input('Informe a idade: '))
    if idade < 0 or idade > 150:
        print('Idade deve estar entre 0 e 150')
while sal <= 0:
    sal = int(input('Informe o salario: '))
    if sal <= 0:
        print('Salario deve ser maior que zero')
while sexo != 'M' and sexo != 'F':
    sexo = input('Informe seu sexo M / F: ').upper()
    if sexo != 'M' and sexo != 'F':
        print('Informe o sexo.')
while ('SCVD'.find(estado_civil) < 0):
    estado_civil = (input('Informe o estado civil: ')).upper()
    if ('SCVD'.find(estado_civil) < 0):
        print( 'Estado civil deve ser informado como S (solteiro), C (casado),'\
            ' V (viuvo) ou D (divorciado)')
print(nome)
print(idade)
print(sal)
print(sexo)
print(estado_civil)

