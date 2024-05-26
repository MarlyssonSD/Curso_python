price = float(input("Digite o valor do produto: "))

escolha = int(input("Como deseja pagar?\n1- Dinheiro ou cheque (Terá 10% de desconto)\n2- À vista no cartão (terá 5% de desconto\n"
                    "3- Até 2x no cartão (preço normal)\n4- 3x ou + no cartão (20% de juros)\nEscolha: "))

print('O produto custa: {}'.format(price))

if escolha == 1:
    print("VALOR FINAL: {}".format(price * 0.9))
elif escolha == 2:
    print("VALOR FINAL: {}".format(price * 0.95))
elif escolha == 3:
    print("VALOR FINAL: {}".format(price))
elif escolha == 4:
    print("VALOR FINAL: {}".format(price * 1.2))