#São estruturas bidimensionais-linha e coluna
#indexando em duas dimensões
#A matriz é vetor com l elmentos, onde cada elemento é um vetor com l elementos


# M = [ [5,3,2], [7,6,1] ]
# print(M)

# M[0][0] = 5  
# M[0][1]= 3
# M[0][2] = 2
# M[1][0] = 7
# M[1][1] = 6
# M[1][2] = 1



LINHAS = 2
COLUNAS = 2

matriz = [[None]*COLUNAS for i in range(LINHAS)]
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz[linha][coluna] = int(input(f'{linha}x{coluna}: '))

# for linha in range(LINHAS):
#     matriz[linha]=[None]*COLUNAS

print(matriz)