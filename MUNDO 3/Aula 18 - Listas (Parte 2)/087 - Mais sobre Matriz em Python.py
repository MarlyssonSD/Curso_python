matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(len(matriz)):
    for y in range(len(matriz)):
        matriz[x][y] = int(input(f'Digite o que deseja guardar na posição {x} {y}: '))

for x in range(len(matriz)):
    print()
    for y in range(len(matriz)):
        print(f'{matriz[x][y]:^5}', end=' ')
print()

soma_pares = 0
soma_terceira_col = 0
maior_segunda_linha = 0

for x in range(len(matriz)):
    for y in range(len(matriz)):
        if matriz[x][y] % 2 == 0:
            soma_pares += matriz[x][y]
        if y == 2:
            soma_terceira_col += matriz[x][y]
        if x == 1:
            if matriz[x][y] > maior_segunda_linha:
                maior_segunda_linha = matriz[x][y]

print(f'Soma dos valores pares: {soma_pares}')
print(f'Soma da terceira coluna: {soma_terceira_col}')
print(f'Maior valor da segunda linha: {maior_segunda_linha}')
