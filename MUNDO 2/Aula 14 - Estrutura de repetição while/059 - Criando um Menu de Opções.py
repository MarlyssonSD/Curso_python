print("Digite 2 valores para efetuar algum processo:")
num1 = int(input("Digite o valor 1: "))
num2 = int(input("Digite o valor 2: "))

escolha = -1
while escolha != 5:
    print("======="*3)
    print("Escolha a ação:")
    print("SOMA [1]\nMULTIPLICAÇÃO[2]\nMAIOR[3]\nTROCAR NÚMEROS[4]\nSAIR[5]")
    print("======="*3)

    escolha = int(input("--> ESCOLHA: "))
    if escolha not in [1,2,3,4,5]:
        print("Opção inválida!")
    if escolha == 1:
        soma = num1 + num2
        print("A soma de {} + {} é igual a: {}".format(num1,num2,soma))

    elif escolha == 2:
        mult = num1 * num2
        print("A multiplicação de {} * {} é igual a: {}".format(num1,num2,mult))

    elif escolha == 3:
        if num1 > num2:
            print("{} é maior que {}".format(num1,num2))
        else:
            print("{} é maior que {}".format(num2,num1))

    elif escolha == 4:
        num1 = int(input("Digite o valor 1: "))
        num2 = int(input("Digite o valor 2: "))

