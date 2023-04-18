n = int(input('Digite a quantidade de numeros: '))
cont = 1

while cont<=n:
    valor = int(input(f'Digite o {cont}° valor: '))
    if valor%2 == 0:
        print(f'{valor} é par')
    else:
        print(f'{valor} é ímpar')
    cont += 1