#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).


arquivo = float(input('Informe o tamanho do arquivo em MB: '))
internet = float(input('Informe a velocidade da sua internet: '))

tamanhoBits = (((arquivo * 1024) * 1024) * 8)
tempoSegundos = tamanhoBits / ((internet * 1024) * 1024)
tempoMinutos = tempoSegundos / 60

print(f'Tempo aproximado de download: {tempoMinutos:.2f} minutos')