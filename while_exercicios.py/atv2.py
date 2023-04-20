#Programa que ler varios numeros ,calcula e exibe a media deles com exceçao do numero 999 que para o programa 

n = int(input('Digite a quantidade de numeros: '))
cont = 0
soma = 0


while cont<n:
    cont += 1
    valor = int(input(f'Digite o {cont}° valor: '))
    soma += valor
    if valor == 999:
        print('Fim do programa!')  
        break  
    media = (soma/n)
    print(f'A media desses numeros é: {media:.2f}')