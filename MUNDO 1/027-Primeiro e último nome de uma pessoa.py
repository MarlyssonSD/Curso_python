nome = str(input('Digite o seu nome completo: ')).strip()
a = nome.split()
print('O seu primeiro nome é: {}'.format(a[0]))
nome2 = nome.rfind(' ')
print('O seu último nome é: {}'.format(nome[nome2:]))
