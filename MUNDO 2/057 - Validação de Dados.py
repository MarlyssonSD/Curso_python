sexo = "a"
while sexo not in 'MF':
    sexo = str(input("Digite o seu sexo (APENAS 'M' OU 'F'): ")).upper().strip()[0]
#maiúsculo, tira espaços e pega apenas a primeira letra

if sexo == 'M':
    print("O seu sexo é o Masculino!")
else:
    print("O seu sexo é o Feminino!")


# #ouuuuuu
# while sexo not in 'MF':
#     # sexo = str(input("Digite o seu sexo (APENAS 'M' OU 'F'): ")).upper().strip()[0]