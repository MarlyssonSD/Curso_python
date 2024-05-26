quantidade = int(input("Para a sequência de Fibonacci, digite a quantidade de termos a serem vistos: "))
primeiro = 1
anterior = 1

while quantidade > 0:
    print("{} -> ".format(primeiro),end='')
    primeiro += anterior
    quantidade -=1

    if quantidade > 0:
        print("{} -> ".format(anterior), end='')
        anterior +=primeiro
        quantidade -=1
print("Acabou")







