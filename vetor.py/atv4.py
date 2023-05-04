QTDE = 10
vetor = [None]*QTDE

for index in range(QTDE):
    vetor[index] = int(input('Digite um valor: '))

    if index%2==0:
        print(f'Numeros em indices pares: {vetor[index]}')

    elif index%2!=0:
        print(f'Numeros em indices impares: {vetor[index]}')