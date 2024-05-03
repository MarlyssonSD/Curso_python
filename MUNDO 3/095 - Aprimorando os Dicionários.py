jogadores = []
jogador = {}
gols_partida = []

flag = 's'

while True:
    gols_partida.clear()
    jogador['nome'] = input('Digite o nome: ')
    quant_partidas = int(input('Digite a quantidade de partidas: '))
    for x in range(1, 1+quant_partidas):
        gols_partida.append(int(input(f'Na {x}ª partida fez quantos gols? ')))
    jogador['quant_gols_partidas'] = gols_partida[:]
    jogador['total_gols'] = 0
    for x in gols_partida:
        jogador['total_gols'] += x
    jogadores.append(jogador.copy())
    flag = input('Continuar? (nao para sair): ')

    if flag in ['n', 'nao', 'não']:
        break

print('====='*15)
print(f'{"Código":<8} {"Nome":<18} {"Gols por partida":<17} {"Total de gols"}')
for cod in range(len(jogadores)):
    print(cod, end=' '*8)
    for v in jogadores[cod].values():
        print(f'{str(v):<20}', end='')
    print()
print('====='*15)

while True:
    escolha_jogador = int(input("Qual jogador deseja visualizar (-1 para sair)? "))
    if escolha_jogador == -1:
        break
    if escolha_jogador < len(jogadores):
        print(f'=-=-=-Levantamento do Jogador: {jogadores[escolha_jogador]["nome"]}-=-=-=')
        for x in range(len(jogadores[escolha_jogador]['quant_gols_partidas'])):
            print(f'No jogo {x+1} fez {jogadores[escolha_jogador]["quant_gols_partidas"][x]} gols')
    else:
        print('=-='*10)
        print('Valor inserido não existe')
        print('=-='*10)
