numeros = [[],[]]

numero = 0
for x in range(7):
    numero = int(input(f'Digite o nº{x+1}: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)

#Sem uso de sort
temp = 0
for x in range(len(numeros[0])):
    for y in range(x+1, len(numeros[0])):
        if numeros[0][x] > numeros[0][y]:
            temp = numeros[0][x]
            numeros[0][x] = numeros[0][y]
            numeros[0][y] = temp

for x in range(len(numeros[1])):
    for y in range(x+1, len(numeros[1])):
        if numeros[1][x] > numeros[1][y]:
            temp = numeros[1][x]
            numeros[1][x] = numeros[1][y]
            numeros[1][y] = temp

#Com sort
#numeros[0].sort()
#numeros[1].sort()

print(f'Números pares digitados: {numeros[0]}')
print(f'Números ímpares digitados: {numeros[1]}')

