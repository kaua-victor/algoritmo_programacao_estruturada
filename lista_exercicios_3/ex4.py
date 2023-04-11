nome = input('Digite seu nome: ').title()
sexo = input('Informe seu sexo: (M)Masculino ou (F)Feminino: ')

# if sexo == 'M' or sexo == 'm':
#     print(f'Olá, Sr. {nome}!')

# elif sexo == 'F' or sexo == 'f':
#     print(f'Olá, Sra. {nome}!')

# else:
#     print(f'{nome}, informou o sexo inadequadamente, corrija!')

match sexo:
    case 'M' | 'm':
        print(f'Olá, Sr. {nome}!')

    case 'F' | 'f':
        print(f'Olá, Sra. {nome}!')

    case _:
         print(f'{nome}, informou o sexo inadequadamente, corrija!')