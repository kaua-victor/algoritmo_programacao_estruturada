frase = input('Digite uma frase: ')
nova = ''
divisao = frase.split()

for i in range(len(divisao)):
    nova += divisao[i]
    
print(f'{nova}')