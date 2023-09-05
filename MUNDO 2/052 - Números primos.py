num = int(input("Digite e descubra se o número é primo: "))
condicao = 0
for x in range(2,num):
    if (num % x == 0):
        print("Não é primo")
        condicao = 1
        break
if condicao == 0:
    print("O número é primo")

print("Fim do programa")

