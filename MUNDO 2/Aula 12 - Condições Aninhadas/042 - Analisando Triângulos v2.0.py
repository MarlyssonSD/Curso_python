a = float(input("Digite o tamanho de um lado do triângulo: "))
b = float(input("Digite o tamanho do segundo lado do triângulo: "))
c = float(input("Digite o tamanho do terceiro lado do triângulo: "))

if a < b + c and b < a + c and c < b + a:
    print("Pode ser formado um triângulo com os valores {}, {} e {}".format(a, b, c))
    if a == b == c:
        print("O triângulo será equilátero")
    elif a == b != c or a == c != b or b == c != a:
        print("O triângulo será isósceles")
    else:
        print("O triângulo será escaleno")
else:
    print("Um triângulo não pode ser formado")
