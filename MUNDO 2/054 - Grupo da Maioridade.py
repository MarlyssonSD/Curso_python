from datetime import date
contagem_maior = 0
contagem_menor = 0

for x in range(1,8):
    n = int(input("Digite o ano de nascimento da {}ª pessoa: ".format(x)))
    if (date.today().year-n) >= 18:
        print("O indivíduo {} é maior de idade".format(x))
        contagem_maior += 1
    else:
        print("O indivíduo {} é menor de idade".format(x))
        contagem_menor += 1
print("São {} menores de idade e {} maiores de idade".format(contagem_menor,contagem_maior))


