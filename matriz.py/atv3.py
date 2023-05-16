from random import randint

n = int(input('Digite a quantidade de linhas e colunas: '))
a = [[None]*n for i in range(n)]
b = [[None]*n for i in range(n)]

for linha in range(n):
    for coluna in range(n):
        a[linha][coluna] = randint(1,20)

print('Primeira matriz gerada:')
for linha in range(n):
    for coluna in range(n):
        print(f'{a[linha][coluna]:4}',end='')
    print()

for linha in range(n):
    for coluna in range(n):
        b[linha][coluna] = a[linha][coluna] + linha+coluna

for linha in range(n):
    for coluna in range(n):
        if b[linha] == b[coluna] or coluna == n-1-linha:
            b[linha][coluna] = 0

print('Segunda Matriz:')
for linha in range(n):
    for coluna in range(n):
        print(f'{b[linha][coluna]:4}', end='')
    print()