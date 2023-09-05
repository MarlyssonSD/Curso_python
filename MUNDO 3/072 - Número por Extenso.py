numeros = ('zero','um', 'dois', 'três','quatro','cinco', 'seis','sete', 'oito', 'nove','dez')


while True:
    escolha = int(input("Escolha um número de 1 - 20 para escrever por extenso (flag: -1): "))
    if (escolha == -1):
        break
    if 0 <= escolha <= 20:
        print(f'O número digitado é {numeros[escolha]}')