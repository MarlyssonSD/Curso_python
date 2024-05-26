from random import randint

player = -1
tentativas = 0
x = randint(0,10)

print("Tente acertar o número do computador (entre 0 e 10): ")
while player != x:
    player = int(input())
    if player != x:
        print("Errooouuuuuu")
        tentativas+=1

print("Parabéns, você acertou, era o número: {}\nVocê precisou de {} tentativas!".format(player,tentativas))