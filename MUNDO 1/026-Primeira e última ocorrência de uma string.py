frase = str(input('Digite uma frase: ')).upper().strip()
print('Na sua frase tem {} letras "a".'.format(frase.count('A')))
print('A primeira letra "a" está na posição {}.'.format(frase.find('A') + 1))
print('A última letra "a" está na posição {}.'.format(frase.rfind('A') + 1))