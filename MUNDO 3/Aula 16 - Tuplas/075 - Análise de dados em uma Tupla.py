print("Digite 4 números: ")
numeros = (int(input()),int(input()),int(input()),int(input()))
numeros_nove = 0
apareceu = 0
for x in range(4):
    if numeros[x] == 9:
        numeros_nove+=1
print(f"Foram {numeros_nove} numeros 9")
if 3 in numeros:
    print(f"O primeiro número 3 está na posição: {numeros.index(3)}")
print(f"Numeros pares: ",end= "")

for x in range(4):
    if numeros[x] % 2 == 0:
        print (numeros[x]   ,end=' ')

