"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no
qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

    8  3  4 
    1  5  9
    6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: 
produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 
parece ser mais simples que usar uma matriz 3x3. 

"""

"""

def qMagico(*n):
    quadradoM = [[],[],[]]
    for l in range(0, 3):
        for c in range(0, 3):
            quadradoM[l][c] = [l],[c]
    
    for l in range(0, 3):
        for c in range(0,3):
            print(f'[{quadradoM[l][c]}]', end='')
            print()

qMagico(0,9,8,7,6,5,4,3,2)


"""

def qudradoM():
    matriz = [[0,0,0],[0,0,0],[0,0,0]]
    for l in range (0, 3):
        for c in range(0,3):
            matriz[l][c] = int(input(f'Digite um valor para [{l},{c}:]'))
    print('-'*30)
    for l in range(0,3):
        for c in range(0,3):
            print(f'[{matriz[l][c]:^5}]', end='')
        print()

resp =qudradoM()