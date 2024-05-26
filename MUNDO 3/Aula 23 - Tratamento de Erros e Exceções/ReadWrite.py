def ler(nome_arq):
    print()
    try:
        print('\033[94m' + '-'*31 + '\033[0m')  # Azul
        print(f'\033[93m{"Nome":<15}\t{"Idade":>15}\033[0m')  # Amarelo
        with open(nome_arq, 'r') as arq:
            for linha in arq:
                print(f'\033[92m{linha.strip()}\033[0m')  # Verde
        print('\033[94m' + '-'*31 + '\033[0m')  # Azul
    except FileNotFoundError:
        print('\033[91mArquivo inexistente ou vazio\033[0m')  # Vermelho


def escreve(nome_arq):
    while True:
        try:
            nome = str(input("Digite o nome: "))
        except:
            print('Nome inválido')
        else:
            break

    while True:
        try:
            idade = int(input("Digite a idade:"))
        except:
            print('Idade inválida')
        else:
            break

    with open(nome_arq, 'a') as arq:
        arq.write(f'{nome:<20}\t{idade:>5} \n')
    print(f'\033[92mNovo cadastro realizado!\033[0m')
