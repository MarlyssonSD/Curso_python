value = soma = quantidade = 0
continuar = ''

value = int(input("Digite valores para serem somados, caso queira parar digite '999': "))
menor = maior = value
while continuar != 'n':
    while value != 999:
        soma += value
        quantidade += 1

        if value > maior:
            maior = value
        if value < menor:
            menor = value
        value = int(input("Digite 999 se quiser parar! "))
    print("A média de todos os {} números digitados foi: {}\nO menor deles foi: {} \nO maior deles foi: {}".format(
        quantidade, soma / quantidade, menor, maior))
    continuar = str(input("Deseja continuar digitando números? ('s' ou 'n'): ")).lower()
    value = 0
