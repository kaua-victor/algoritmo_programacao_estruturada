QTDE = 10
vetor = [None]*QTDE

for index in range(QTDE):
    vetor[index] = int(input('Digite um valor: '))

print('Elementos em posiçoes pares:')
for index in range(QTDE):

    if index%2==0:
        print(f'{vetor[index]}')

print('Elementos em posiçoes impares:')
for index in range(QTDE):
    
    if index%2!=0:
        print(f'{vetor[index]}')