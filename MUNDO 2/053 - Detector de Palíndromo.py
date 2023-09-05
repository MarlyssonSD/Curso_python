frase = str(input("Digite algo para descobrir se é um palíndromo: ")).lower()
frase = frase.replace(" ","")

if (frase == frase[::-1]):
     print(frase," ----> É um palíndromo")
else:
     print("Não é um palíndromo")

