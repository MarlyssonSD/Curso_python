nome = str(input('Digite o seu nome completo: ')).strip()
a = nome.split()
b = a[0]
print('Nome maiúsculo: {}'.format(nome.upper()))
print('Nome minúsculo: {}'.format(nome.lower()))
print('A quantidade de letras no nome é: {}'.format(len(nome)- nome.count(' ')))
print('No primeiro nome tem {} letras'.format(len(b)))