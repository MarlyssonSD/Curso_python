km = float(input('Informe a distância percorrida pelo carro em Km: '))
dias = int(input('Informe por quantos dias o carro foi alugado: '))
valor = 0.15 * km + 60 * dias
print('O total a ser pago será de R${:.2f}'.format(valor))