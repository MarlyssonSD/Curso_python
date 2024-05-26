numero = int(input("Digite um valor: "))
choose = int(input('Digite a conversão desejada:\n1- binário\n2- octal\n3- hexadecimal:\n '))

if choose == 1:
    print("O número {} em binário é: {} ".format(numero, bin(numero)[2:]))

elif choose == 2:
    print("O número {} em octal é: {} ".format(numero, oct(numero)[2:]))

elif choose == 3:
    print("O número {} em hexadecimal é: {} ".format(numero, hex(numero)[2:]))