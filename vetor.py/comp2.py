n = int(input('Digite a quantidade de elementos: '))

a = []
b = []
c = []

print('Criando vetor A')
for index in range(n):
    a.append(int(input('Digite um valor: ')))
print(f'Vetor lido: {a}')

print('Criando vetor B')
for index in range(n):
    b.append(int(input('Digite um valor: ')))
print(f'Vetor lido: {b}')

for index in range(n):
    c.append(a[index])
    c.append(b[index])

print(f'Novo vetor: {c}')




