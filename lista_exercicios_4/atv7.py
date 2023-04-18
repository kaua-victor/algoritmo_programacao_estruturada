#Programa para saber se um numero e´ primo

numero = int(input('Digite um número: '))

if numero <=1:
    print('Não é primo!')
else:
    eh_primo = True
    for i in range(2,numero):
        if numero%i==0:
            eh_primo = False
    if eh_primo:
        print(f'{numero} é primo!')
    else:
        print(f'{numero} não é primo!')