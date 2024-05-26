distancia = float(input("Digite a distância da sua viagem em KM: "))
if distancia <=200:
    valor = distancia*0.50
    print("O valor da viagem será: {:.2f}".format(valor))
else:
    valor = distancia*0.45
    print("O valor da viagem será: {:.2f}".format(valor))