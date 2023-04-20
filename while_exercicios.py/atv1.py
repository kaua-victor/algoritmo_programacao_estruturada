numeros = 30
cont = 0
soma = 0

while cont<numeros:
    cont += 1
    valor = int(input(f'Digite o {cont}° valor: '))
    soma += valor

print(f'A soma de todos os valores é: {soma}')