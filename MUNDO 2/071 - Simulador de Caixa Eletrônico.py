value = int(input("Digite o valor que deseja sacar: R$"))
if value >= 50:
    print(f"Serão {value//50} notas de R$50")
    value = value % 50
if value >= 20:
    print(f"Serão {value//20} notas de R$20")
    value = value % 20
if value >= 10:
    print(f"Serão {value//10} notas de R$10")
    value = value % 10
if value >= 1:
    print(f"Serão {value//1} notas de R$1")
    value = value % 1
