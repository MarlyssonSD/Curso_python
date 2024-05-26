def ficha(nome='<vazio>', gols=0):
    print(f'O jogador {nome} fez {gols} gols')


nome_jogador = input("Digite o nome do jogador: ")
gols_jogador = input("Quantos gols foram feitos? ")

if gols_jogador.isnumeric():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0

if nome_jogador.strip() == '':
    ficha()
else:
    ficha(nome_jogador, gols_jogador)

