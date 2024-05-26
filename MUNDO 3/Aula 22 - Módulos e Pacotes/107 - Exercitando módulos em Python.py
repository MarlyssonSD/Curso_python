import moeda as m

porcent = 10
v = float(input("Digite um valor: "))

print(f'O valor {v} será aumentado em {porcent}%: {m.aumentar(v, porcent)}')
print(f'O valor {v} será diminuído em {porcent}%: {m.diminuir(v, porcent)}')
print(f'O valor {v} será dividido pela metade: {m.metade(v)}')
print(f'O valor {v} será dobrado: {m.dobro(v)}')
