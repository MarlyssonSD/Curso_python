ano = int(input("Digite um ano: "))

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            print("O Ano é bissexto")
        else:
            print("O Ano não é bissexto")
    else:
        print("O Ano é bissexto")
else:
    print("O Ano não é bissexto")


