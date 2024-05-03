jogador = {}
gols_partida = []

jogador['nome'] = input('Digite o nome: ')
jogador['quant_partidas'] = int(input('Digite a quantidade de partidas: '))
for x in range(1, 1+jogador['quant_partidas']):
    gols_partida.append(int(input(f'Na {x}ª partida fez quantos gols? ')))

jogador['quant_gols_partidas'] = gols_partida

jogador['total_gols'] = 0
for x in gols_partida:
    jogador['total_gols'] += x

for c, v in jogador.items():
    print(f'{c}: {v}')
for x in range(len(gols_partida)):
    print(f'Na {x+1}ª partida fez {gols_partida[x]} gols ')