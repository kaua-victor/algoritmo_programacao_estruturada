numero = int(input('Digite um número: '))
#def factorial(num): 
#    if num < 0: 
#        print('Fatorial de negativo não existe')
#
#   elif num == 0: 
#        return 1
#        
#    else: 
#        fact = 1
#        while(num > 1): 
#            fact *= num 
#            num -= 1
#       return fact 
 
#print(f'Fatorial de {num} é {factorial(num)}')

fatorial = 1
for k in range(2,numero+1):
    fatorial *= k

print(f'{numero}! = {fatorial}')