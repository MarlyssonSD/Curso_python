from random import randint

pontuacao = 0
while True:
    num_computer = randint(1, 10)
    escolha_i_p = str(input("Quer ímpar ou par? (digite I ou P): \n")).strip().lower()

    if escolha_i_p == 'i' or escolha_i_p == 'p':

        if escolha_i_p == 'i':
            print("O computador é PAR")
            num_player = int(input("Escolha o seu número: "))
            print('-----'*10)
            if ((num_computer+num_player)%2) == 1:
                pontuacao += 1
                print(f"{num_computer} + {num_player} = {num_player+num_computer} é ÍMPAR, o player tem {pontuacao} pontos")
            else:
                print(f"{num_computer} + {num_player} = {num_player+num_computer} é PAR, o player perdeu com {pontuacao} pontos")
                break

        elif escolha_i_p == 'p':
            print("O computador é ÍMPAR")
            num_player = int(input("Escolha o seu número: "))
            print('-----'*10)

            if ((num_computer + num_player) % 2) == 0:
                pontuacao += 1
                print(
                    f"{num_computer} + {num_player} = {num_player + num_computer} é PAR, o player tem {pontuacao} pontos")
            else:
                print(
                    f"{num_computer} + {num_player} = {num_player + num_computer} é ÍMPAR, o player perdeu com {pontuacao} pontos")
                break

        else:
            print("O computador é ÍMPAR")
    else:
        print("Digite uma opção válida!!")
        print('-'*35)
