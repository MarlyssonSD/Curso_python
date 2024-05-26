
def notas(* notas):
    ''' -Envie quantas notas desejar e obtenha informações sobre:
    -quantidade de notas, maior nota, menor nota e a média '''
    dados = {}
    menor = 11
    maior = 0
    quantidade_notas = 0
    media = 0

    for x in notas:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
        media += x
    media = media/len(notas)

    dados['notas'] = len(notas)
    dados['maior'] = maior
    dados['menor'] = menor
    dados['media'] = media
    return dados


dicionario = notas(6, 9.5, 3, 5.2, 9)
help(notas)
print(dicionario)

