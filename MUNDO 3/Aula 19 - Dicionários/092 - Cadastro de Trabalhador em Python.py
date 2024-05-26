from datetime import datetime

ano_atual = datetime.now().year

dados = {}

dados['nome'] = input('Digite o nome: ')
ano_nasc = int(input('Digite o ano de nascimento: '))
dados['idade'] = ano_atual - ano_nasc
dados['carteira de trabalho'] = int(input('Digite o nome (0 caso não tenha) : '))

if dados['carteira de trabalho'] != 0:
    dados['ano de contratação'] = int(input('Digite o ano da contratação: '))
    dados['salário'] = input('Digite o salário: ')
    dados['aposentadoria'] = dados['ano de contratação'] + 35 - ano_nasc
print('=-='*10)
for c, v in dados.items():
    print(f'{c}: {v}')


