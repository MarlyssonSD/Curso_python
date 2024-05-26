def leiaint(frase):
    flag = True
    while True:
        try:
            num = int(input(frase))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor.')
            return 0
        except:
            print('Você não digitou um número inteiro.')
            continue
        else:
            return num


def leiafloat(frase):
    flag = True
    while True:
        try:
            num = float(input(frase))
        except KeyboardInterrupt:
            print('O usuário preferiu não digitar o valor.')
            return 0
        except:
            print('Você não digitou um número float.')
            continue
        else:
            return num


nint = leiaint('Digite um número: ')
nfloat = leiafloat('Digite um número: ')

print(f'O inteiro digitado foi {nint} e o float foi {nfloat}')