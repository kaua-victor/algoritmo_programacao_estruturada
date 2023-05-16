from random import randint

n = int(input('Digite a quantidade de linhas e colunas: '))
matriz = [[None]*n for i in range(n)]

for linha in range(n):
    for coluna in range(n):
        matriz[linha][coluna] = randint(1,20)

print('Matriz gerada:')
for linha in range(n):
    for coluna in range(n):
        print(f'{matriz[linha][coluna]:4}',end='')
    print()

print('Elementos da diagonal principal:')
for linha in range(n):
    for coluna in range(n):
        if [linha]==[coluna]:
            print(f'{matriz[linha][coluna]:4}',end='')
        