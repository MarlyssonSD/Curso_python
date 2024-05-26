def aumentar(valor=0, porcentagem=0, formatacao=True):
    valor = valor * (1 + porcentagem/100)
    if formatacao:
        return moeda(valor)
    return valor


def diminuir(valor=0, porcentagem=0, formatacao=True):
    valor -= valor * (porcentagem/100)
    if formatacao:
        return moeda(valor)
    return valor


def dobro(valor=0, formatacao=True):
    if formatacao:
        return moeda(valor*2)
    return valor*2


def metade(valor=0, formatacao=True):
    if formatacao:
        return moeda(valor/2)
    return valor/2


def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')


def resumo(valor=0, porcentagem1=0, porcentagem2=0):
    print(f'O valor {moeda(valor)} será dividido pela metade: {metade(valor, True)}')
    print(f'O valor {moeda(valor)} será dobro: {dobro(valor, True)}')
    print(f'O valor {moeda(valor)} será aumentado em {porcentagem1}%: {aumentar(valor, porcentagem1)}')
    print(f'O valor {moeda(valor)} será diminuído em {porcentagem2}%: {diminuir(valor, porcentagem2)}')
