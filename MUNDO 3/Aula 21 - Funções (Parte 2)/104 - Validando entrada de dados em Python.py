def leiaint(frase):

    num = input(frase)
    while not num.isnumeric():
        print('Você não digitou um número.')
        num = input(frase)

    return int(num)


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')