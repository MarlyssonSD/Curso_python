from time import sleep


def contador(inicio, fim, intervalo):
    if intervalo < 0:
        intervalo = -intervalo

    if intervalo != 0:
        if inicio < fim:
            pass
        else:
            intervalo = -intervalo
        print('~~'*20)
        print(f'Contagem de {inicio} até {fim} em {intervalo} em {intervalo}: ')
        for x in range(inicio, fim, intervalo):
            print(f'{x}', end=' ')
            # sleep(0.5)
        print('  _FIM_')
        print('~~'*20)
    else:
        print("Intervalo 0? aí não né meu chapakkkkkkk")


contador(1, 10, 1)
contador(10, 0, 2)
ini = int(input("Digite o início: "))
final = int(input("Digite o final: "))
interv = int(input("Digite o intervalo: "))

contador(ini, final, interv)
