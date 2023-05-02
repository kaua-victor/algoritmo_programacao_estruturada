tamanho = int(input('Digite a quantidade de numeros: '))
a = [None]*tamanho

for index in range(tamanho):
    a[index] = int(input('Numero: '))

k = int(input('Digite um multiplicador: '))

b = [None]*tamanho

for index in range(tamanho):
    b[index] = a[index]*k

print(a,b)