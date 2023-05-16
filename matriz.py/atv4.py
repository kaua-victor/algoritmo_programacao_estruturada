from random import randint

LINHAS = 3
COLUNAS = 5
matriz1 = [[None]*COLUNAS for i in range(LINHAS)]
matriz2 = [[None]*LINHAS for i in range(COLUNAS)]


for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz1[linha][coluna] = randint(1,20)

print('Primeira Matriz:')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{matriz1[linha][coluna]:4}',end='')
    print()

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz2[coluna][linha] = matriz1[linha][coluna]

print('Segunda Matriz:')
for coluna in range(COLUNAS):
    for linha in range(LINHAS):
        print(f'{matriz2[coluna][linha]:4}',end='')
    print()