house_value = int(input("Digite o valor da casa: "))
salary = int(input('Digite o salário do comprador: '))
years_to_pay = int(input('Digite em quantos anos pretende pagar: ')) * 12
#monthly = mensal

monthly_price =  house_value/years_to_pay

if monthly_price > (salary * 1.3):
    print('Transação não pode ser efetuada, prestação ficará maior que 30% do seu salário\n Prestação: {:.2f}'.format(monthly_price))
else:
    print("A prestação ficará no valor de: R${:.2f} e pagará por 10 anos a casa no valor de R${} ".format(monthly_price,house_value))
