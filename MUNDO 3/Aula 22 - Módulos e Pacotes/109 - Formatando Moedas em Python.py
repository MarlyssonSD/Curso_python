import moeda as m

porcent = 10
v = float(input("Digite um valor: "))

print(f'O valor {m.moeda(v)} será aumentado em {porcent}%: {m.aumentar(v, porcent, True)}')
print(f'O valor {m.moeda(v)} será diminuído em {porcent}%: {m.diminuir(v, porcent, False)}')
print(f'O valor {m.moeda(v)} será dividido pela metade: {m.metade(v, True)}')
print(f'O valor {m.moeda(v)} será dobro: {m.dobro(v, False)}')
