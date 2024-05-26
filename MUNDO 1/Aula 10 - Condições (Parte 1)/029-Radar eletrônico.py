velo = int(input("Digite a velocidade do seu veículo: "))
if velo>80:
    velo = (velo-80)*7
    print("\nVocê ultrapassou o limite de velocidade e receberá uma multa de {:.1f} reais".format(velo))
else:
    print("\nVocê estava no limite de velocidade!")

