print("\t-=-=-=-Progressão aritmética-=-=-=-")

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
quantidade = 10
print("Os {} primeiros termos dessa PA é:".format(quantidade))
if razao != 0:
    while quantidade >= 0:
        print("{} -> ".format(primeiro_termo) if quantidade != 1 else "{} FIM.".format(primeiro_termo), end='')
        primeiro_termo += razao
        quantidade -= 1
        if quantidade == 0:
            quantidade = int(input("\nDeseja visualizar mais termos? "))

else:
    print("A razão 0 não é válida")