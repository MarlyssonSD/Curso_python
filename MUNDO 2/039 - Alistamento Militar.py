from datetime import date
#caso importe tudo ----> import datetime faça ---> year = datetime.date.today().year

year = date.today().year

age = year - int(input("Qual o ano de seu nascimento:\n"))

if age < 18:
    print("Você precisará se alistar em {} anos".format(18 - age))
elif age == 18:
    print("Você precisa se alistar")
elif age > 18:
    print("Você ja deveria ter se alistado há {} anos".format(age - 18))
