number = 0
lista = []
lista_par = []
lista_impar = []

print("Digite números para adicionar em uma lista (SAIR == -1): ")
while True:
    number = int(input())
    if number != -1:
        lista.append(number)
    else:
        print("Saímos do while")
        break

for x in range(0, len(lista)):
    if lista[x] % 2 == 1:
        lista_impar.append(lista[x])
    else:
        lista_par.append(lista[x])

print(f" Lista Completa {lista}")
print(f" Lista de pares {lista_par}")
print(f" Lista de ímpares {lista_impar}")

