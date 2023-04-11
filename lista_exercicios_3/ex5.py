SALARIO_MINIMO = 1320
COMISSAO = 0.05

total_vendas = float(input('Total vendas: '))

salario = total_vendas*COMISSAO

if salario<SALARIO_MINIMO:
    salario = SALARIO_MINIMO

print(f'Seu salário é: {salario}')