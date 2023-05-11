LINHAS = 2
COLUNAS = 3

a = [[None]*COLUNAS for i in range(LINHAS)]
b = [[None]*COLUNAS for i in range(LINHAS)]

print('Entre com os elemmetos da matriz A:')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        a[linha][coluna] = int(input(f'Matriz A [{linha}][{coluna}]: '))

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        b[linha][coluna] = a[linha][coluna]*2

print(f'\n Matriz A = {a}')

print(f'\n Matriz B = {b}')
print()

print('Matriz A:')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{a[linha][coluna]:4}',' ',end='')
    print()

print('Matriz B:')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{b[linha][coluna]:4}',' ',end='')
    print()