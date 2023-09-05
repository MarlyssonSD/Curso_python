from math import sin,cos, tan, pi
a = float(input('Digite um ângulo qualquer: '))
b = a*(pi/180)
print('O ângulo é igual a {:.2f}sen {:.2f}cos {:.2f}tg'.format(sin(b), cos(b),tan(b)))