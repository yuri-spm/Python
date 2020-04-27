"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo,
 a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes 
 da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário 
 digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do 
 clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que: 
"""

clientes = dict()
cadastro = list()
resp = 1
while resp != 0:
    clientes['Codigo'] = int(input('Codigo:' ))
    if clientes['Codigo'] == 0:
        break
    clientes['Altura'] = float(input('Altura:' ))
    clientes['Peso'] = float(input('Peso:' ))
    cadastro.append(clientes.copy)

print(cadastro)
print(clientes)