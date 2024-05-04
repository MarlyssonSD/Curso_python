from time import sleep


def maior(*numeros):
    print('=-='*20)
    num_maior = 0
    print('Analisando números: ')
    for x in numeros:
        print(x, end=' ')
        if x > num_maior:
            num_maior = x
        sleep(0.2)

    print(f'Fora informados {len(numeros)} números ao todo.')
    print(f'O maior valor informado foi: {num_maior}')
    print()


maior(3, 5, 6, 1, 7, 23, 11, 4)
maior(2, 9, 4, 5, 7, 1)
maior(6, 2, 54, 10)
maior()
