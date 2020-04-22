"""
<<<<<<< HEAD
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""



=======
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""

>>>>>>> 32ade59e1243ef048b0f708a02fcf42c37b55242
cantidato1 = 0
cantidato2 = 0
cantidado3 = 0

n = int(input('Nº de eleitores: '))
print('1 - CANDIDATO 1 \n2 - CANDIDARTO 2 \n3 - CANDIDATO 3')
for c in range(0, n):
    resp = int(input('Informe o numero do candidato:'))
    if resp == 1:
        cantidato1 += 1
    elif resp == 2:
        cantidato2 += 1
    else:
        cantidado3 += 1

print(f'O canditato 1 teve {cantidato1}. \nO candidto 2 teve {cantidato2}. \nO candidato 3 teve {cantidado3}')