lista = []

print("Digite números para adicionar em uma lista (SAIR == -1): ")
while True:
    number = int(input())
    if number != -1:
        lista.append(number)
    else:
        print("Saímos do while")
        break

print(f"{len(lista)} Números foram escritos")
lista.sort(reverse=True)
print(f"Ordem decrescente: {lista}")

if 5 in lista:
    print("Sim, existe o número 5 na lista")
else:
    print("Não, não existe o número 5 na lista")
