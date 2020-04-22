"""

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém
    não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá
    ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada
    pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
    pagamento, valor do desconto e valor a pagar.


"""
print()
print('HIPERMERCADO TABAJARA'. center(60))
resp = int(input('TIPOS DE CARNE\n1 - FILE DUPLO \n2 - ALCATRA \n3 - PICANHA \nOPÇÃO: ' ))
if resp == 1:
    qkg = float(input('KG: '))
    if qkg  < 5:
        tkg = qkg * 4.9

    else:
        tkg = qkg * 5.8

if resp == 2:
    qkg = float(input('KG: '))
    if qkg  < 5:
        tkg = qkg * 5.9

    else:
        tkg = qkg * 6.8

if resp == 3:
    qkg = float(input('KG: '))
    if qkg  < 5:
        tkg = qkg * 6.9

    else:
        tkg = qkg * 7.8

fpagamento = input('Forma de pagamento no cartão da loja [SIM/ NAO]:  ').upper()
if 'SIM' in fpagamento:
    tkg = tkg * 0.95
    print(f'O valor total a pagar e {tkg:.2f}')
else:
<<<<<<< HEAD
    print(f'O valor total a pagar e {tkg}')
=======
    print(f'O valor total a pagar e {tkg}')
    

>>>>>>> 8a690647c7dfadec9dde21f72d8b7227561dddd6
