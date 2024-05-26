palavras = ('Jogar', 'mario','delicia', 'legal', 'bonito', 'filosofia', 'comida')

for x in range (len(palavras)-1):
    print(f"Na palavra: '{palavras[x]}' Temos as vogais: ",end='')
    for y in range(len(palavras[x])-1):
        if (palavras[x][y] in 'aeiou'):
            print(palavras[x][y],end=' ')
    print('\n')