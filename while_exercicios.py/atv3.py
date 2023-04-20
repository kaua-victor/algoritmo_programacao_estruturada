FLAG = 0

valor = int(input(f'Digite um valor: '))
menor = maior = valor

while valor != FLAG:

    if valor > maior:
        maior = valor

    elif valor < menor:
        menor = valor

    valor = int(input(f'Digite outro valor: '))

print(f'O maior valor é {maior} e o menor valor é {menor}')