maior = -6500

for k in range(20):
    
    valor = int(input(f'Digite o {k+1}° valor: '))
    if valor>maior:
        maior=valor

print(f'Maior valor fornecido: {maior}')