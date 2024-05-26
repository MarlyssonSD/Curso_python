import moeda as m

porcent = 10
v = float(input("Digite um valor: "))

#NÃO FUNCIONA COM AS ATUALIZAÇÕES SOLICITADAS DURANTES OS DESAFIOS USE O *109*
print(f'O valor {m.moeda(v)} será aumentado em {porcent}%: {m.moeda(m.aumentar(v, porcent))}')
print(f'O valor {m.moeda(v)} será diminuído em {porcent}%: {m.moeda(m.diminuir(v, porcent))}')
print(f'O valor {m.moeda(v)} será dividido pela metade: {m.moeda(m.metade(v))}')
print(f'O valor {m.moeda(v)} será dobro: {m.moeda(m.dobro(v))}')
