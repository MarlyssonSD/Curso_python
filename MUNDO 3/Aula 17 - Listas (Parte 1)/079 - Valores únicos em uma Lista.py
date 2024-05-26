number = 0
lista = []

print("Digite números para adicionar em uma lista (SAIR = -1): ")
while(number != -1):
    number = int(input())
    if  number != -1 and not number in lista:
        lista.append(number)
lista.sort()
print(lista)



