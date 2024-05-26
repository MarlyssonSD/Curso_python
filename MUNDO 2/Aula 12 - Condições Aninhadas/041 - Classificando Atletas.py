from datetime import date

idade = date.today().year - int(input("Digite seu ano de nascimento: "))

if idade <= 9:
    print("{} anos: MIRIM".format(idade))
elif 9 < idade <= 14:
    print("{} anos: INFANTIL".format(idade))
elif 14 < idade <= 19:
    print("{} anos: JUNIOR".format(idade))
elif idade ==20:
    print("{} anos: SÊNIOR".format(idade))
else:
    print ("{} anos: MASTER".format(idade))
