hodo_antes=float(input('Digite o valor do hodometro antes da viagem: '))
hodo_dps=float(input('Digite o valor do hodometro depois da viagem: '))
numero_de_l_gastos=float(input('Digite o numero de litros gastos: '))
preço_lcombustivel=float(input('Digite o preço do litro do combustivel: '))
capacidade_do_tanque=float(input('Digite a capacidade do tanque em litros: '))

kmrod=hodo_dps-hodo_antes
print(f'a) Quilometragem rodada: {kmrod} ')

kmlit=kmrod/numero_de_l_gastos
print(f'b) Quilometros por litro do veiculo: {kmlit:.2f} ')

aut=capacidade_do_tanque*kmlit
print(f'c) Autonomia do veiculo: {aut:.2f} ')

custv=preço_lcombustivel*numero_de_l_gastos
print(f'd) Custo da viagem: {custv:.2f} ')