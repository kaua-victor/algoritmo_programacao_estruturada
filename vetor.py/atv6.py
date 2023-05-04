tamanho = int(input('Digite a quantidade de numeros: '))
v = [None]*tamanho


for k in range(tamanho):
    v[k] = int(input('Digite um valor: '))
    v.reverse()

print(f'{v}')