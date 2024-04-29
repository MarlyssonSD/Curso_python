matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for x in range(len(matriz)):
    for y in range(len(matriz)):
        matriz[x][y] = int(input(f'Digite o que deseja guardar na posição {x} {y}: '))

for x in range(len(matriz)):
    print()
    for y in range(len(matriz)):
        print(f'{matriz[x][y]:^5}', end=' ')
