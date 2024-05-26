from random import randint
numeros = (randint(0,100),randint(0,100),randint(0,100),randint(0,100),randint(0,100))

print("Os números sorteados foram: ")
for x in range (5):
    print(numeros[x],end=' ')

maior = 0
menor = 0
for x in range (5):
    if x == 0:
        maior = numeros[x]
        menor = numeros [x]
    if numeros[x] > maior:
        maior = numeros[x]
    if numeros[x] < menor:
        menor = numeros[x]
print("\nO número maior é:",maior)
print("O número menor é:",menor)
