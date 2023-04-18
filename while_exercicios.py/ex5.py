valor = int(input('Digite um valor: '))
soma = 0

while valor !=0:
    soma += valor
    if soma >100:
        break  
    valor = int(input('Digite outro valor: '))
          
print(f'A soma de todos os valores é: {soma}')