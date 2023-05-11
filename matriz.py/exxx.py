from random import randint


qtde_linhas = int(input('Qual a quantidade der linhas? '))
qtde_colunas = int(input('Qual a quantidade der colunas? '))
cont = 0
matriz = [[None]*qtde_colunas for i in range(qtde_linhas)]


for linha in range(qtde_linhas):
    for coluna in range(qtde_colunas):
        matriz[linha][coluna] = randint(1,20)

for linha in range(qtde_linhas):
    for coluna in range(qtde_colunas):
        print(f'{matriz[linha][coluna]:4}',' ',end='')
    print()

maior=matriz[0][0]
for linha in range(qtde_linhas):
    for coluna in range(qtde_colunas):
        if matriz[linha][coluna] > maior:
            maior = matriz[linha][coluna]
            
for linha in range(qtde_linhas):
    for coluna in range(qtde_colunas):
        if matriz[linha][coluna] == maior:
            print(f'{linha}x{coluna}')
            cont+=1

print(f'\n O maior é {maior} e ele aparece {cont} vez(es).')