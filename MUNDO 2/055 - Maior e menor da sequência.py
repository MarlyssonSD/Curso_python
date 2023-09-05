maior = 0
menor = 0
for x in range(1,6):
    peso = float(input("Digite o peso {}: ".format(x)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O menor peso é: {} \nO maior peso é: {}".format(menor,maior))