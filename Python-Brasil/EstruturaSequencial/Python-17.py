#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#   comprar apenas latas de 18 litros;
#   comprar apenas galões de 3,6 litros;
#   misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para
#   cima, isto é, considere latas cheias.

"""

tamanho = float(raw_input('Quantos metros quadrados devem ser pintados: '))

litros = (tamanho / 6.0) * 1.1  # 10% de folga
latas = int(litros / 18.0)
galoes = int(litros / 3.6)

# Calculo de latas
if (litros % 18 != 0):
    latas += 1

# Calculo de galoes
if (litros % 3.6 != 0):
    galoes += 1

# Calculo misturando latas e galoes
mixLatas = int(litros / 18.0)
mixGaloes = int((litros - (mixLatas * 18.0)) / 3.6)
if ((litros - (mixLatas * 18.0) % 3.6 != 0)):
    mixGaloes += 1

print 'Latas:', latas, '. Valor:', latas * 80
print 'Galoes:', galoes, '. Valor:', galoes * 25
print 'Latas:', mixLatas, 'e', mixGaloes, '. Valor: ', \
    (mixLatas * 80)+(mixGaloes*25)


"""



tamanho = float(input('Informe o tamanho da area: '))
litros = tamanho / 3.0
if litros <= 3.6:
    latas = (litros / 3.6)
    if litros % 3.6 != 0:
        latas += 1
        print(f'Serão necessárias: {latas:.0f} galões')
        vgaloes = latas * float(80)
        print(f'Valor total a pagar {vgaloes:.2f}')
else:
    latas = (litros / 18.0)
    if litros % 18 != 0:
        latas += 1
        print(f'Serão necessárias: {latas:.0f} latas')
        vlatas = latas * float(25)
        print(f'Valor total a pagar {vlatas:.2f}')



