import ReadWrite as rw

def menu():
    print('\033[94m' + '='*30 + '\033[0m')  # Azul
    print('\033[92m1 - Listar pessoas cadastradas\033[0m')  # Verde
    print('\033[93m2 - Cadastrar pessoa\033[0m')  # Amarelo
    print('\033[91m3 - Sair\033[0m')  # Vermelho
    print('\033[94m' + '='*30 + '\033[0m')  # Azul



nome_arquivo = 'lista_pessoas.txt'
flag = True
while flag:
    menu()
    try:
        escolha = int(input('Escolha: '))
    except:
        print('Escolha inválida')
    else:
        if escolha in [1, 2, 3]:
            if escolha == 1:
                rw.ler(nome_arquivo)
            elif escolha == 2:
                rw.escreve(nome_arquivo)
            elif escolha == 3:
                flag = False
                continue
        else:
            print('Número inválido')

print(f'\033[91mPrograma finalizado!\033[0m')
print(f'\033[91m--\033[0m')

