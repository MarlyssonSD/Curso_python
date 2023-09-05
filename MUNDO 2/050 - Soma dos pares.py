soma = 0
print("Digite 6 valores: ")
for n in range(0,6):
    n = int(input())
    if (n % 2 == 0):
        soma +=n
print("A soma dos números pares digitados é: {} ".format(soma))