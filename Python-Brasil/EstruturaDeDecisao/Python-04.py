#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra do alfabeto: ').upper()

if letra in'AEIOU':
    print('Vogal')
else:
    print('Consoante')