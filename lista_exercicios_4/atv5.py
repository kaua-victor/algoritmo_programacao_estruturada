numero = int(input('Digite o numero de pessoas: '))

sexo_masc=0
sexo_fem=0

for k in range(numero):
    sexo = input('Digite o sexo -M ou F: ').upper()

    if sexo=='M':
        sexo_masc += 1

    elif sexo=='F':
        sexo_fem += 1

percent_masc = (sexo_masc/numero)*100
percent_fem = (sexo_fem/numero)*100

print(f'O percentual de homens é: {percent_masc}. O percentual de mulheres é: {percent_fem}')