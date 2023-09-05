print("\t-=-=-=-Progressão aritmética-=-=-=-")

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))


print("Os 10 primeiros termos dessa PA é:")

for x in range(1,11):
    print("Termo {}: {} ".format(x, primeiro_termo))
    primeiro_termo += razao
