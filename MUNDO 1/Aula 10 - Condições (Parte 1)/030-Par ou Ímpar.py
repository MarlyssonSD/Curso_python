numero = int(input("Digite um número inteiro: "))
div = numero%2

if numero == 0:
    print("O número digitado foi 0, ele é ímpar ou par???")
elif div == 1:
    print("O número digitado é ímpar")
elif div == 0:
    print("O número digitado é par")
print(div)
