from random import randint


LINHAS = 2
COLUNAS = 2

matriz = [[None]*COLUNAS for i in range(LINHAS)]
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz[linha][coluna] = randint(1,100)

print(matriz)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(matriz[linha][coluna],' ',end='')
    print()