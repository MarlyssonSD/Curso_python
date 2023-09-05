l = float(input('Informe a largura da sua parede em metros: '))
c = float(input('Agora informe o comprimento em metros: '))
print('A área total da parede é de {:.3f}m² e precisará {:.3f} litros de tinta para pintá-la'.format(l*c, (l*c)/2))