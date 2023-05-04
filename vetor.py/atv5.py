tamanho = int(input('Digite a quantidade de numeros: '))
v = [None]*tamanho
maior = -65000
menor = 65000
indicemaior = 0
indicemenor = 0

for i in range(tamanho):
    v[i] = int(input('Digite um valor: '))

for index in range(tamanho):
    if v[index] > maior:
        maior = v[index]
        indicemaior = index
    elif v[index] < menor:
        menor = v[index]
        indicemenor = index

print(f'O maior numero é {maior} no indice {indicemaior} e o menor numero é {menor} no indice {indicemenor}. ')