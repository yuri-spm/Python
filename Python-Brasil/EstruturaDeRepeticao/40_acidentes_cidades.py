"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

    Código da cidade;
    Número de veículos de passeio (em 1999);
    Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
    Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
    Qual a média de veículos nas cinco cidades juntas;
    Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. 

"""

cidade = []

for c in range(0, 2):
  cadastro = {}
  cadastro['Cidade'] = int(input('Codigo da Cidade: '))
  cadastro['Veiculos'] = int(input('Quantidade Veiculos de passeio: '))
  cadastro['Acidentes'] = int(input('Quantidades de acidentes em 1999: '))
  cidade.append(cadastro)  

print()
for info in cadastro.keys() :
  print(f'{info:>2}\t\t ', end='')
print()

for k, v in enumerate(cidade):
  for n in v.values():
    print(f' {(n):<20}', end='')
  print()
print('-=-'*20)
