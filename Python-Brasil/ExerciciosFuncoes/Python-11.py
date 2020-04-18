"""
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e
devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e
retorne NULL caso a data seja inválida.
"""
from datetime import date
def dataValida (dia, mes, ano):
    if dia < 0 or dia > 31 and  mes < 0 or mes > 12:
        return False
    
    else:
        return True

   
    
    


ndate = input('Informe uma data: ')
dia = int(ndate[:2])
mes = int(ndate[3:5])
ano = int(ndate[6:10])

resp = dataValida(dia, mes, ano)
print( resp)

