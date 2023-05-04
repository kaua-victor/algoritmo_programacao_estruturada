# tamanho = int(input('Digite a quantidade de numeros: '))
# v = [None]*tamanho
# maior = -65000
# menor = 65000
# indicemaior = 0
# indicemenor = 0

# for i in range(tamanho):
#     v[i] = int(input('Digite um valor: '))

# for index in range(tamanho):
#     if v[index] > maior:
#         maior = v[index]
#         indicemaior = index
#     elif v[index] < menor:
#         menor = v[index]
#         indicemenor = index

# print(f'O maior numero é {maior} no indice {indicemaior} e o menor numero é {menor} no indice {indicemenor}. ')

tamanho = int(input('Digite a quantidade de numeros: '))
v = [None]*tamanho
indicemaior = 0
indicemenor = 0

for i in range(tamanho):
    v[i] = int(input('Digite um valor: '))

menor = maior = v[0]

for i in range(1,tamanho):
    if v[i]>maior:
        maior=v[i]
        indicemaior=i
    if v[i]<menor:
        menor=v[i]
        indicemenor=i

print(f'Menor = {menor} no indice {indicemenor} e maior = {maior} no indice {indicemaior}')