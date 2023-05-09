n = int(input('Digite a quantidade de elementos: '))
vetor = [None]*n
contpar = 0
contimpar = 0

for index in range(n):
    vetor[index] = int(input('Digite um valor: '))

    if vetor[index]%2==0:
        contpar+=1

    if vetor[index]%2!=0:
        contimpar+=1

soma = sum(vetor)
media = soma/2

print(f'A quantidade de elementos pares são: {contpar}.')
print(f'A quantidade de elementos impares são: {contimpar}.')
print(f'A soma de todos os elementos é: {soma}.')
print(f'A média dos elementos do vetor é: {media}')