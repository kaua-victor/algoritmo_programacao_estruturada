#vetor[indice,começando no 0]
#vetor->list

QTDE = 5
valores = [None]*QTDE

soma = 0
for k in range(QTDE):
    valores[k] = int(input('Digite um valor: '))
    soma += valores[k]

media = soma/QTDE
print(f'Media = {media:.2f}')
print('Valores acima da media:', end='')

for index in range(QTDE):
    if valores[index]>=media:
        print(valores[index],' ')
