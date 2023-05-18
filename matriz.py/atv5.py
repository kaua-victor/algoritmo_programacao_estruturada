LINHAS = 20
COLUNAS = 4
matriz = [[None]*COLUNAS for i in range(LINHAS)]
soma = media = media_geral = cont = soma_media=0

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if coluna != 3:
            matriz[linha][coluna] = int(input('Digite suas notas: '))
            soma+=matriz[linha][coluna]
        elif coluna == 3:
            media = soma/3
            soma_media+=media
            matriz[linha][coluna] = media
    soma = media = 0

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        media_geral = (soma_media/20)

for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        if coluna == 3 and matriz[linha][coluna] > media_geral:
            cont+=1


print('Notas :')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{matriz[linha][coluna]:4}',end='')
    print()

print('Média geral da turma:')
print(f'{media_geral}')
print()

print('Números de alunos acima da média:')
print(f'{cont}')