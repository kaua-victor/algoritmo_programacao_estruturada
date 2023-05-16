from random import randint

LINHAS = 2
COLUNAS = 3
a = [[None]*COLUNAS for i in range(LINHAS)]
b = [[None]*COLUNAS for i in range(LINHAS)]
c = [[None]*COLUNAS for i in range(LINHAS)]

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        a[linha][coluna] = randint(1,20)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        b[linha][coluna] = randint(1,20)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        c[linha][coluna] = a[linha][coluna] + b[linha][coluna]

print('Primeira Matriz')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{a[linha][coluna]:4}',end='')
    print()

print('Segunda Matriz')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{b[linha][coluna]:4}',end='')
    print()

print('Matriz da sooma das duas matrizes anteriores')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{c[linha][coluna]:4}',end='')
    print()