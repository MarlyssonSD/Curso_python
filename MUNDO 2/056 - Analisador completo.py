media_idade = 0.0
homem_mais_velho = 'a'
idade_h_mais_velho = 0
mulheres_sub_20 = 0
for x in range(1,5):
        nome = str(input("Digite o nome da {}ª pessoa: ".format(x)))
        idade = int(input("Digite a idade da {}ª pessoa: ".format(x)))
        sexo = str(input("Digite o sexo da {}ª pessoa ('M' OU 'F'): ".format(x))).upper()

        media_idade +=idade
        if sexo == 'M':
                if idade > idade_h_mais_velho:
                        homem_mais_velho = nome
                        idade_h_mais_velho = idade
        if sexo == 'F' and idade < 20:
                mulheres_sub_20 += 1

media_idade = media_idade/4

print("Temos uma média de idade de:",media_idade,"anos"
      "\nO homem mais velho tem {} anos e se chama {}".format(idade_h_mais_velho,homem_mais_velho),
      "\nE temos",mulheres_sub_20,"mulheres com menos de 20 anos")

