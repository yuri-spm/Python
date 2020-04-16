"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
 Valide a entrada e permita repetir a operação.

"""
while True:

    popA = int(input('Informe o tamanho da população A: '))
    crescA = float(input('Informe a taxa de crescimento: '))
    popB = int(input('Informe o tamanho da população B: '))
    crescB = float(input('Informe a tava de crescimento: '))
    cont = 0
    if popA > popB:
        while popA > popB:
            popA *= crescA
            popB *= crescB
            cont +=1
        print(f'A população de B vai ser maior que a população de A em {cont}')
    else:

        while popB > popA:
            popA *= crescA
            popB *= crescB
            cont += 1
        print(f'A população de A vai ser maior que a população de B em {cont} ')
    resp = input('Para sair digite SAIR: ').upper()[0]
    if resp in 'SAIR':
        break


