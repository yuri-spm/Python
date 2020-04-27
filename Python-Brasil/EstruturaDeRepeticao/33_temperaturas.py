"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. 
"""



temperaturas = list()

n = int(input('Informe a quantidade de temperaturas: '))
for c in range(1,n+1):
    resp = int(input(f'{c+1}º temperatura: '))
    temperaturas.append(resp)

print(f'O maior numero da lista foi {max(temperaturas)} e o menor foi {min(temperaturas)}')
print(f'A media das temperaturas foi {(sum(temperaturas)/len(temperaturas)):.0f}')

