pessoa = []
pessoas = []

mais_pesadas = []
mais_leves = []
maior_peso = 0
menor_peso = 500
nome = ''
peso = 1

while peso != 0:
    nome = input("Digite o nome: ")
    peso = float(input("Digite o peso (0 para finalizar): "))
    if peso == 0:
        break
    else:
        pessoa.append(nome)
        pessoa.append(peso)
        pessoas.append(pessoa[:])
        pessoa.clear()

for p in pessoas:
    if p[1] >= maior_peso:
        maior_peso = p[1]
    if p[1] <= menor_peso:
        menor_peso = p[1]

for p in pessoas:
    if menor_peso == p[1]:
        mais_leves.append(p[0])
    if maior_peso == p[1]:
        mais_pesadas.append(p[0])

print(f'O total de pessoas foi {len(pessoas)}.')
print(f'O maior peso foi {maior_peso}, da(s) pessoa(s): {mais_pesadas}')
print(f'O menor peso foi {menor_peso}, da(s) pessoa(s): {mais_leves}')

