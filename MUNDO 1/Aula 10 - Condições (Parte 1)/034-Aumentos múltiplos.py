salario = float(input("Digite o salário que será aumentado: "))

if salario>1250:
    salario = salario*1.1
    print("O novo salário com aumento é: {:.2f}".format(salario))
else:
    salario = salario*1.15
    print("O novo salário com aumento é: {:.2f}".format(salario))

