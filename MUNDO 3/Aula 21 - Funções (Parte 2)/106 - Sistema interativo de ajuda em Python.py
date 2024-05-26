#SEM CORES
def ajuda(comando):
    print('='*50)
    help(comando)
    print('='*50)


while True:
    palavra = input('Digite o comando que tem dúvida: ').lower()
    if palavra == 'fim':
        break
    ajuda(palavra)

print('Programa finalizado.')
