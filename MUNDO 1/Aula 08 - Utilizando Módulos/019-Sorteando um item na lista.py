import random
a1 = str(input('Digite o nome do primeiro aluno:'))
a2 = str(input('Segundo: '))
a3 = str(input('Terceiro: '))
a4 = str(input('Quarto: '))
alunos = [a1, a2, a3, a4]
print('O aluno escolhido foi {}!'.format(random.choice(alunos)))