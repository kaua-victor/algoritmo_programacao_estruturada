quantidade = int(input('Informe quantos números serão fornecidos: '))

somatorio = 0
for k in range(quantidade):
    valor = int(input(f'Digite o {k+1}° valor: '))
    somatorio = somatorio + valor
print(f'O somatorio é {somatorio}')