cidade = []
cadastro = {}
for c in range(0, 2):
    cadastro['Cidade'] = int(input('Codigo da Cidade: '))
    cadastro['Veiculos'] = int(input('Quantidade Veiculos de passeio: '))
    cadastro['Acidentes'] = int(input('Quantidades de acidentes em 1999: '))
    cidade.append(cadastro.copy)
    cadastro.clear


print()
for info in cadastro.keys() :
    print(f'{info:>2}\t\t ', end='')
print()

for k, v in enumerate(cadastro):
    for n in v.values():
        print(f'{str(n):<15}', end='')
    print()
print('-=-'*20)



