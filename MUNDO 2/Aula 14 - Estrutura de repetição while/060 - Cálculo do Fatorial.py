fat = int(input("Digite um número para calcular o fatorial: "))
result = 1

#MODO 1
# while fat != 0:
#     result *= fat
#     fat = fat-1
# print("O fatorial de é: {}". format(result))

#MODO 2
# print("Calculo:")
# while fat != 0:
#     result *= fat
#     print("{}".format(fat),end='')
#     if fat != 1:
#         print("x",end=' ')
#     if fat == 1:
#         print("= {}".format(result))
#     fat = fat - 1

#MODO 3
print("Calculo de {}!:".format(fat))
while fat != 0:
    result *= fat
    print("{}".format(fat),end=' ')
    print("x " if fat > 1 else '= ',end='')
    fat = fat-1
print(result)

