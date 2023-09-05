maior_18 = homens = mulher_sub20 = 0

while True:
    idade = int(input("Digite a idade da pessoa: "))
    sexo = ' '

    while sexo not in 'fm':
        sexo = str(input("Digite o sexo Feminino/Masculino (apenas F ou M): ")).strip().lower()

    if idade > 18:
        maior_18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulher_sub20 += 1

    continuar = ' '
    while continuar not in 'naosim':
        continuar = str(input("Deseja continuar? ")).lower()
    if continuar in 'n' 'nao' 'não':
        break
print(f"São {maior_18} pessoas maiores de 18 anos, {homens} homem(ns) e {mulher_sub20} mulheres que possuem menos de 20 anos")