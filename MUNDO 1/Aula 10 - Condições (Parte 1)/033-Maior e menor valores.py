n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o primeiro número: "))
n3 = float(input("Digite o primeiro número: "))
if n1 < n2:
    if n1 < n3:
        print("O menor número é o {}".format(n1))
    else:
        print("O menor número é o {}".format(n3))
elif n2 < n3:
    print("O menor número é o {}".format(n2))
else:
    print("O menor número é o {}".format(n3))

if n1 > n2:
    if n1 > n3:
        print("O maior número é o {}".format(n1))
    else:
        print("O maior número é o {}".format(n3))
elif n2 > n3:
    print("O maior número é o {}".format(n2))
else:
    print("O maior número é o {}".format(n3))



