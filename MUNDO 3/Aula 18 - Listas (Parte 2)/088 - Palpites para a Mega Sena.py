from random import randint
from time import sleep

lista_jogos = []
lista_numeros = []
quant_jogos = int(input("Quantos jogos deseja? "))
num = parada = 0

print(f'\n-=-=Listando {quant_jogos} jogos!=-=-')
for x in range(quant_jogos):
    while parada != 6:
        num = randint(1,60)
        if not (num in lista_numeros):
            lista_numeros.append(num)
            parada += 1
    parada = 0
    lista_jogos.append(lista_numeros[:])
    lista_numeros.clear()
    print(f'Jogo {x+1}: {lista_jogos[x]}')
    sleep(1)

