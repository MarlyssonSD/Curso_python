colocados = ('Palmeiras', 'Internacional','Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR', 'Atlético-MG',
             'chapecoense', 'Fortaleza', 'São Paulo', 'América-MG') #etc

print("-=-=-=" * 4)
print("Os quatro primeiros colocados:\n")
for cont in range(1, 5):
    print(f"{cont}º {colocados[cont]}")
print("-=-=-="*4)
for cont in range(-1, -5, -1):
    print(f"{colocados[cont]}")
print("-=-=-="*4)
print(f"{sorted(colocados)}")
print("-=-=-="*4)
print(f'posição: {colocados.index("chapecoense")}')