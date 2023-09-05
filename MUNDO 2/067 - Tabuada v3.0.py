while True:
    tabuada = int(input("Digite um número para ver a tabuada (para SAIR digite um número negativo): "))
    n = 0
    if tabuada < 0:
        break

    while n <= 10:
        print(f"{n} x {tabuada} = {n*tabuada}")
        n += 1
