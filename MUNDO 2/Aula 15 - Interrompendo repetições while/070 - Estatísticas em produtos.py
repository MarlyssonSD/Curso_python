gasto_total = maior_1000 = mais_barato = contagem = 0
nome_mais_barato = ' '
while True:
    nome = str(input("Digite o nome do produto: ")).strip()
    value = int(input("Digite o valor do produto: R$"))

    gasto_total += value
    if value > 1000:
        maior_1000 += 1

    if contagem == 0 or value < mais_barato:
        nome_mais_barato = nome
        
    continuar = ' '
    while continuar not in 'naosim':
        continuar = str(input("Deseja continuar: "))
    if continuar in 'nao':
        break
    contagem += 1
print(f"Custo final de {gasto_total} reais, tem {maior_1000} itens mais caros que R$1000 e {nome_mais_barato} é o mais barato")
