from random import randint
from time import sleep
#import para ordenar de forma "Automática"
from operator import itemgetter

jogadores = {}
ranking_jogadores = {}
num_random = 0
nome_jogador = 'jogador'

for x in range(1, 5):
    num_random = randint(1, 6)
    jogadores[nome_jogador+str(x)] = num_random
    print(f'{nome_jogador+str(x)} pegou {num_random}')
    sleep(1)

#forma "Manual"
for x in range(6, 0, -1):
    for chave, valores in jogadores.items():
        if valores == x:
            ranking_jogadores[chave] = jogadores[chave]
print('=-=-='*10)

#Forma "Automática"
#Transformará em uma lista, deve transformar para dicionário OU utilizar enumarate no FOR
ranking_jogadores = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True))


posicoes = 1
for c, v in ranking_jogadores.items():
    print(f'{posicoes}º Lugar - {c} com {v}')
    posicoes += 1
