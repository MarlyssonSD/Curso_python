import random
rand = random.randint(0, 5)
numero = int(input('Digite um número de 0 a 5: '))
if numero == rand:

    print("\nO computador pensou no número {}!!!\nVocê venceu, PARABÉNS".format(rand))
else:
    print("O computador pensou no número {}!\nVocê perdeu!".format(rand))