#math possui um comando só para o calculo da hipotenusa ----> math.hypot(cateto1, cateto2)
from math import pow, sqrt
opos = float(input('Digite o cateto oposto: '))
adj = float(input('Informe o cateto adjacente: '))
hipo = sqrt(pow(opos,2) + pow(adj, 2))
print('O valor da hipotenusa com os catetos {} e {} é igual a {:.3f}'.format(opos,adj,hipo))