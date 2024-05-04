from random import  randint


def sorteio(numeros):
    print(f'Sorteando os valores: ', end='')
    for x in range(5):
        num = randint(1,10)
        numeros.append(num)
        print(f'{num}', end=' ')
    print()

def somaPar(numeros):
    soma_pares = 0
    for x in numeros:
        if x % 2 == 0:
            soma_pares += x
    print(f'Somando os números pares da lista: {numeros} = {soma_pares} ')


numeros = []
sorteio(numeros)
somaPar(numeros)