from random import randint
escolha = int(input("Escolha qual a sua jogada:\n1- PAPEL \U0000270B \n2- PEDRA \U0000270A \n3- TESOURA \U0000270C\nESCOLHA: "))

numero_random = randint(1,3)

if escolha == 1:
    if numero_random == 2:
        print("Você GANHOU escolhendo PAPEL \U0000270B! O computador escolheu PEDRA \U0000270A")
    elif numero_random == 3:
        print("Você PERDEU escolhendo PAPEL \U0000270B! O computador escolheu TESOURA \U0000270C")
    else:
        print("EMPATOU ambos escolheram PAPEL \U0000270B")
elif escolha == 2:
    if numero_random == 1:
        print("Você PERDEU escolhendo PEDRA \U0000270A! O computador escolheu PAPEL \U0000270B")
    elif numero_random == 3:
        print("Você GANHOU escolhendo PEDRA \U0000270A! O computador escolheu TESOURA \U0000270C")
    else:
        print("EMPATOU ambos escolheram PEDRA \U0000270A")
elif escolha == 3:
    if numero_random == 1:
        print("Você GANHOU escolhendo TESOURA \U0000270A! O computador escolheu PAPEL \U0000270B")
    elif numero_random == 2:
        print("Você PERDEU escolhendo TESOURA \U0000270A! O computador escolheu PEDRA \U0000270C")
    else:
        print("EMPATOU ambos escolheram TESOURA \U0000270A")