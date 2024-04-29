lista = []
for x in range(0, 5):
   lista.append(int(input(f"Digite o valor da posição {x}:")))

menor = min(lista)
maior = max(lista)
print(f"O MENOR número foi {menor} nas posições: ", end='')
for x in range(0, 5):
    if menor == lista[x]:
        print(f"{x}... ", end='')

print(f"\nO MAIOR número foi {maior} nas posições: ", end='')
for x in range(0, 5):
    if maior == lista[x]:
        print(f"{x}...", end='')