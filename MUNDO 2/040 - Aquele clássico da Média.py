nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado!\n Com media: {} ".format(media))
elif 5 <= media < 7:
    print("Recuperação\n Com media: {}".format(media))
elif 7 <= media:
    print("Aprovado por média!\n Com media: {}".format(media))