a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))


if a > b:
    print("{} é maior que {}".format(a,b))
elif a < b:
    print("{} é menor que {}".format(a,b))
else:
    print("Os valores são iguais!")