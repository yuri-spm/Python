"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                          Até 5 Kg           Acima de 5 Kg
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade
    (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""

tmorangos = int(input('Kg de morangos: '))
tmaca = int(input('Kg maçã: '))
tkg = tmorangos + tmaca

if tmorangos <= 5: 
    vmorango = tmorangos * 2.5
else:
    vmorango = tmorangos * 2.2

if tmaca <= 5:    
    vmaca = tmaca * 2.5
else:
    vmaca  = tmaca * 1.5


vtotal = vmorango + vmaca

if tkg > 8 or vtotal > 25:
    vtotal = vtotal * 0.9



print(f'Valor total : {vtotal}')