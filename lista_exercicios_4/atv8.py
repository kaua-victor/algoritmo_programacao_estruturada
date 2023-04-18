#Programa que calcula o maior quadrado perfeito

import math
numero = int(input('Digite um número: '))

maior_quadrado_perfeito = 1

for k in range(2,numero+1):
    raiz = math.sqrt(k)
    if int(raiz)==raiz and k>maior_quadrado_perfeito:
        maior_quadrado_perfeito=k

print(f'O maior quadrado perfeito é {maior_quadrado_perfeito}')