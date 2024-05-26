pessoas = []
pessoa = {}
flag = 's'

while True:
    pessoa['nome'] = input('Digite o nome: ')
    pessoa['sexo'] = input('Digite o sexo (M/F): ').lower()
    pessoa['idade'] = int(input('Digite o idade: '))
    pessoas.append(pessoa.copy())
    flag = input('Continuar? (nao para sair): ')
    if flag in ['n', 'nao', 'não']:
        break

quantidade_pessoas = len(pessoas)
media_idade = 0
lista_mulheres = []

for x in pessoas:
    media_idade += x['idade']
    if x['sexo'] == 'f':
        lista_mulheres.append(x['nome'])
print(media_idade)
pessoas_acima_media = []
media_idade = media_idade/quantidade_pessoas
for x in pessoas:
    if x['idade'] > media_idade:
        pessoas_acima_media.append(x['nome'])

print('=-='*10)
print(f'Tem {quantidade_pessoas} pessoas')
print(f'A média da idade é {media_idade} anos')


print(f'As mulheres são: ',end='')
for nome in lista_mulheres:
    print(f'{nome}', end=', ')

print()
print('Pessoas acima da média de idade: ')
for x in pessoas_acima_media:
    print(x, end=' - ')
