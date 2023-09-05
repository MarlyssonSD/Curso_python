value = soma = quantidade = 0

print("Digite valores para serem somados, caso queira parar digite '999'")
value = int(input())

while value != 999:
        soma +=value
        quantidade +=1
        value = int(input())
print("A soma de todos os {} números digitados foi: {}".format(quantidade,soma))
