lado_1 = int(input('Digite a primeira medida: '))
lado_2 = int(input('Digite a segunda medida: '))
lado_3 = int(input('Digite a terceira medida: '))

if lado_1 == lado_2 == lado_3:
    print ('Triângulo equilátero')

elif (lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1):
    print ('Triângulo isósceles')

else:
    print ('Triângulo escaleno')