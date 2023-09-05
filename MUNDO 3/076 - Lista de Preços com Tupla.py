produto_valor = ('maça', 2.99, 'calabresa', 10.99, 'batata', 4.99, 'computador', 2900, 'celular', 1124)
y = 0
print(f"PRODUTO ............. VALOR")
for x in range (len(produto_valor)-5):

    print(f'{produto_valor[y]:.<21}.',end='')
    print(f"{produto_valor[y+1]}")
    y += 2