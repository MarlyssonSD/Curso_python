from math import pow
massa = float(input("Informe a sua massa: "))
altura = float(input("Informe a sua altura: "))

imc = massa/(pow(altura,2))

if imc < 18.5:
    print("Com {:.1f} de IMC o indivíduo está abaixo do peso ".format(imc))
if 18.5 <= imc < 25:
    print("Com {:.1f} de IMC o indivíduo está com o peso ideal".format(imc))
if 25 <= imc < 30:
    print("Com {:.1f} de IMC o indivíduo está com Sobrepeso".format(imc))
if 30 <= imc < 40:
    print("Com {:.1f} de IMC o indivíduo está com Obesidade".format(imc))
if 40 <= imc:
    print("Com {:.1f} de IMC o indivíduo está com Obesidade mórbida".format(imc))
