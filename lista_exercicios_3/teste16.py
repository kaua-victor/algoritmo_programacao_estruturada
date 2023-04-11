valor_1 = int(input('Digite um numero: '))
valor_2 = int(input('Digite outro numero: '))
valor_3 = int(input('Digite outro numero: '))

if valor_1>valor_2 and valor_1>valor_3:
    print(f'O maior é: {valor_1}')

elif valor_2>valor_1 and valor_2>valor_3:
    print(f'O maior é: {valor_2}')

else:
    print(f'O maior é: {valor_3}')