nome = input('Digite seu nome: ').title()
conceito = input('Informe seu conceito: ').title()

if conceito == 'A':
    print(f'Parabéns, {nome}, você é fortemente recomendado!')

elif conceito == 'B' or conceito == 'C':
    print(f'Muito bem, {nome}, você é recomendado!')

elif conceito == 'D':
    print(f'{nome}, você não é recomendado.')

else:
    print(f'{nome}, você informou um conceito não reconhecido.')