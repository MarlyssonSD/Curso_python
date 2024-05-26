num = int(input("Digite o número que você deseja a tabuada"))

for x in range(0,11):
    print("{} x {} = {}".format(num, x, x * num))