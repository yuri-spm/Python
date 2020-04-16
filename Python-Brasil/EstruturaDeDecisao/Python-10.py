#Faça um Programa que pergunte em que turno você estuda.
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print(('Escolha uma opção: '
       'M - MATUTINO   '
       'V - VESPERINO   '
       'N - NOTURNO'))
resp = input('Sua resposta: ').upper()
if resp in "M":
       print('Bom dia')
elif resp in "V":
       print('Boa tarde')
else:
       print('Boa noite')