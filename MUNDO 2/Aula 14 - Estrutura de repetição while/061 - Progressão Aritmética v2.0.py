print("\t-=-=-=-Progressão aritmética-=-=-=-")

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))
control = 0
print("Os 10 primeiros termos dessa PA é:")

while control < 10:
    print("{} -> ".format(primeiro_termo) if control < 9 else "{} -> FIM.".format(primeiro_termo),end='')
    primeiro_termo +=razao
    control +=1
