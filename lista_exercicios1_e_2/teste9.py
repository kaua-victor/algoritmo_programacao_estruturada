SALARIO_FIXO=1000
nv=input('Nome do vendedor: ')
x=int(input('Quantidade de carros vendidos: '))
COMISSAO=200*x
vt=float(input('Valor total das vendas: '))
salfinal= SALARIO_FIXO+COMISSAO+0.05*vt
print(f'O vendedor {nv} vendeu {x} carros esse mês,com um valor total de vendas de {vt:.2f}. Por isso seu salário foi: {salfinal:.2f}')