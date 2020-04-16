#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Informe o seu sexo [M / F]: ').upper()[0]
if sexo in "M":
    print('Sexo Masculino')
elif sexo in 'F':
    print('Sexo Feminimo')
else:
    print('Sexo Invelido')